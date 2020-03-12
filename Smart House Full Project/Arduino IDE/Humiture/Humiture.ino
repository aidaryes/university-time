#include <DHTesp.h>
#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include <ArduinoJson.h>

DHTesp dht;
const int dhtPin = D5;
const int smokePin = A0;

const int ledforTemp = D6;
const int ledforHumid = D7;
const int ledforGas = D8;

char ssid[] = "NUGuest";
char wifi_password[] = "1234512345";

//char ssid[] = "NEW_POINT";
//char wifi_password[] = "wxgg-hd7b-hhd0";

//char ssid[] = "qq";
//char wifi_password[] = "qwertyuio";

//HERE
//const char* host = "10.3.18.142";
const char* host = "68.183.214.100";
const int httpPort = 8080;

int statTemp = -1;
int constTemp = 0;

int statHumid = -1;
int constHumid = 0;

void setup() {
  Serial.begin(115200);
  
  pinMode(ledforTemp, OUTPUT);
  pinMode(ledforHumid, OUTPUT);
  pinMode(ledforGas, OUTPUT);

  pinMode(dhtPin, INPUT);
  pinMode(smokePin, INPUT);
  
  WiFi.begin(ssid, wifi_password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(5000);
    Serial.println("Waiting for connection");
  }
  
  delay(5000);
  Serial.println("Setup done");
  dht.setup(dhtPin, DHTesp::AUTO_DETECT);

  digitalWrite(ledforTemp, HIGH);
  digitalWrite(ledforHumid, HIGH);
  digitalWrite(ledforGas, HIGH);
  delay(5000);

  digitalWrite(ledforTemp, LOW);
  digitalWrite(ledforHumid, LOW);
  digitalWrite(ledforGas, LOW);
  delay(5000);
}

void loop() {  
  
  float temperature = dht.getTemperature();
  statTemp = askTempCmd();
  if( statTemp == 0 && constTemp == 1){
    constTemp = 0;
    digitalWrite(ledforTemp, LOW);
    Serial.println("TEMP OFF");
  }
  else if(statTemp == 1 && constTemp ==0)
  {
    constTemp = 1;
    digitalWrite(ledforTemp, HIGH);
    Serial.println("TEMP ON");
  }
  if (isnan(temperature)) {
    Serial.println("Failed to read Temperature!");
    return;
  }
  Serial.print("Temp: ");
  Serial.println(temperature);

  float humidity = dht.getHumidity();
  statHumid = askHumidCmd();
  if( statHumid == 0 && constHumid == 1){
    constHumid = 0;
    digitalWrite(ledforHumid, LOW);
    Serial.println("HUMID OFF");
  }
  else if(statHumid == 1 && constHumid ==0)
  {
    constHumid = 1;
    digitalWrite(ledforHumid, HIGH);
    Serial.println("HUMID ON");
  }
  if (isnan(humidity)) {
    Serial.println("Failed to read Humidity!");
    return;
  }
  Serial.print("Humidity: ");
  Serial.println(humidity);

  float smokedetection = analogRead(smokePin)/10;
  if(smokedetection > 900) {
    digitalWrite(ledforGas, HIGH);
  } else {
    digitalWrite(ledforGas, LOW);
  }
  if (isnan(smokedetection)) {
    Serial.println("Failed to read from MQ-2 sensor!");
    return;
  }
  Serial.print("Smoke sensor: ");
  Serial.println(smokedetection);

  delay(5000);
  
  if(WiFi.status()== WL_CONNECTED) {      
      String dataTemp = dataFormat("Temp", temperature);
      sendFormat(dataTemp);
      delay(3000);

      String dataHumid = dataFormat("Humid", humidity);
      sendFormat(dataHumid);
      delay(3000);

      String dataGas = dataFormat("Gas", smokedetection);
      sendFormat(dataGas);
      delay(3000);
   } else {  
      Serial.println("Error in WiFi connection");   
   }

   delay(15000);
   
   Serial.println();
   Serial.println("Data from the new iteration:");
}

String dataFormat(String sensorType, float sensorData) {
  String data = "{";
  data = String(data+"\"owner\":");
  data = String(data+"1");
  
  data = String(data+",\"sensortype\":");
  data = String(data+"\"");
  data = String(data+sensorType);
  data = String(data+"\"");
  
  data = String(data+",\"data\":");
  data = String(data+sensorData);

  data = String(data+",\"attached_status\":");
  if(sensorType == "Temp")
  {
    data = String(data+constTemp);
  }
  else if(sensorType == "Humid")
  {
    data = String(data+constHumid);
  }
  else if(sensorType == "Gas")
  {
    data = String(data+"-1"); 
  }
  
  data = String(data+",\"date\":");
  data = String(data+"\"\"");
  data = String(data+"}");
  
  return data;
}

void sendFormat(String data) {
  WiFiClient ourClient;
  if (!ourClient.connect(host, 8080)) {
    Serial.println("Connection failed!");
    return;
  }

//HERE  
  ourClient.println("POST /data/ HTTP/1.1");
  ourClient.println("Host: 68.183.214.100");
  
  ourClient.println("Accept: */*");
  ourClient.println("Content-Type: application/json");
  
  ourClient.print("Content-Length: ");
  ourClient.println(data.length());
  ourClient.println();
  ourClient.print(data);
}

int askTempCmd(){
   if (WiFi.status() == WL_CONNECTED) {
 
    HTTPClient http;

//HERE 
    http.begin("http://68.183.214.100:8080/commands/1/temp/");
    int httpCode = http.GET();
 
    if (httpCode > 0) {
 
      String payload = http.getString();
      Serial.println(payload);
      
      StaticJsonBuffer<200> jsonBuffer;
      JsonObject& root = jsonBuffer.parseObject(payload);

//Change
      delay(2000);
      
      if (!root.success()) {
//Pochemu
          //Serial.println("parseObject() Temp failed");
          return -1;
      }
      
      Serial.print("Status: ");
      long stat = root["status"];

      HTTPClient http;

//HERE
      http.begin("http://68.183.214.100:8080/commands/1/temp/accepted");
      int httpCode = http.GET();
      Serial.print("Status:");
      Serial.println(stat);
      return stat;
    }
 
    http.end();
  }
  return -1;
}

int askHumidCmd(){
  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;

//HERE    
    http.begin("http://68.183.214.100:8080/commands/1/humid/");
    int httpCode = http.GET();
 
    if (httpCode > 0) {
 
      String payload = http.getString();
      Serial.println(payload);

      StaticJsonBuffer<200> jsonBuffer;
      JsonObject& root = jsonBuffer.parseObject(payload);

//Change
      delay(2000);
      
      if (!root.success()) {
//Pochemu        
          //Serial.println("parseObject() Humid failed");
          return -1;
      }
      Serial.print("HUMIStatus: ");
      long stat = root["status"];
      Serial.println(stat);
      HTTPClient http;

//HERE      
      http.begin("http://68.183.214.100:8080/commands/1/humid/accepted");
      int httpCode = http.GET();
      return stat;
    }
 
    http.end();
  }
  return -1;
}
