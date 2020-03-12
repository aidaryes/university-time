import React from 'react';
import {
  View,
  Text,
  StyleSheet,
  ActivityIndicator,
  ScrollView,
  RefreshControl,
  Switch,
  TextInput,
  TouchableHighlight,
  Alert,
} from 'react-native';

var addressInWeb = 'http://68.183.214.100:8080';

export default class ControlPanel extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      temp: '',
      humid: '',
      gas: '',

      bodyTemp: '',
      diasPres: '',
      sysPres: '',

      dataForTemp: [],
      dataForHumid: [],
      dataForGas: [],

      tempTurnOnOff: false,
      humidTurnOnOff: false,
      gasTurnOnOff: false,

      shouldActivAc: false,
      shouldActivHumid: false,

      tempStatus: 0,
      humidStatus: 0,

      loading: true,
      refreshing: false,
    };
  }

  componentDidMount() {
    this.loadData();
  }

  loadData = async () => {
    this.setState({
      loading: true,
    });

    await fetch(
      addressInWeb + '/data/' + this.props.screenProps.userId + '/temp/'
    )
      .then(response => response.json())
      .then(dataForTemp => {
        this.setState({
          dataForTemp: dataForTemp,
        });
      })
      .catch(error => {
        console.error(error);
      });

    await fetch(
      addressInWeb + '/data/' + this.props.screenProps.userId + '/humid/'
    )
      .then(response => response.json())
      .then(dataForHumid => {
        this.setState({
          dataForHumid: dataForHumid,
        });
      })
      .catch(error => {
        console.error(error);
      });

    await fetch(
      addressInWeb + '/data/' + this.props.screenProps.userId + '/gas/'
    )
      .then(response => response.json())
      .then(dataForGas => {
        this.setState({
          dataForGas: dataForGas,
        });
      })
      .catch(error => {
        console.error(error);
      });

    let tempSize = this.state.dataForTemp.length;
    let tempStat = this.state.dataForTemp[tempSize - 1].attached_status;
    let shouldActivateTemp = this.state.dataForTemp[tempSize - 1].shouldActivate;

    let humidSize = this.state.dataForHumid.length;
    let humidStat = this.state.dataForHumid[humidSize - 1].attached_status;
    let shouldActivateHumid = this.state.dataForHumid[humidSize - 1].shouldActivate;

    let gasSize = this.state.dataForGas.length;
    let gasStat = this.state.dataForGas[gasSize - 1].attached_status;

    let tempData = this.state.dataForTemp[tempSize - 1].data;
    let humidData = this.state.dataForHumid[humidSize - 1].data;
    let gasData = this.state.dataForGas[gasSize - 1].data;

    this.setState({
      temp: tempData,
      humid: humidData,
      gas: gasData,
    });

    if(shouldActivateTemp == 0) {
      this.setState({ 
        shouldActivAc: false,
      });
    } else {
      this.setState({
        shouldActivAc: true,
      });
    }

    if(shouldActivateHumid == 0) {
      this.setState({ 
        shouldActivHumid: false,
      });
    } else {
      this.setState({
        shouldActivHumid: true,
      });
    }

    if (tempStat === 0) {
      this.setState({
        tempTurnOnOff: false,
        tempStatus: tempStat,
      });
    } else {
      this.setState({
        tempTurnOnOff: true,
        tempStatus: tempStat,
      });
    }

    if (humidStat === 0) {
      this.setState({
        humidTurnOnOff: false,
        humidStatus: humidStat,
      });
    } else {
      this.setState({
        humidTurnOnOff: true,
        humidStatus: humidStat,
      });
    }

    if (gasStat === 1) {
      this.setState({
        gasTurnOnOff: true,
      });
    }

    this.setState({
      loading: false,
      refreshing: false,
    });
  };

  handleRefresh = () => {
    this.setState(
      {
        refreshing: true,
      },
      () => {
        this.loadData();
      }
    );
  };

  postMethod = (command, status) => {
    fetch(addressInWeb + '/commands/', {
      method: 'POST',
      headers: {
        Accept: 'application/json',
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        fromuser: this.props.screenProps.userId,
        date: '2018-11-07T01:59:00Z',
        command: command,
        status: status,
      }),
    })
      .then(response => response.json())
      .then(responseData => {
        console.log(
          'POST Response',
          'Response Body -> ' + JSON.stringify(responseData)
        );
      })
      .catch(error => {
        console.error(error);
      });
  };

  handleCommand = async command => {
    if (command === 'Temp') {
      if (this.state.tempStatus === 0) {
        this.postMethod(command, 1);
        this.setState({
          tempTurnOnOff: true,
          tempStatus: 1,
        });
      } else {
        this.postMethod(command, 0);
        this.setState({
          tempTurnOnOff: false,
          tempStatus: 0,
        });
      }
    }
    if (command === 'Humid') {
      if (this.state.humidStatus === 0) {
        this.postMethod(command, 1);
        this.setState({
          humidTurnOnOff: true,
          humidStatus: 1,
        });
      } else {
        this.postMethod(command, 0);
        this.setState({
          humidTurnOnOff: false,
          humidStatus: 0,
        });
      }
    }
  };

  handleSaveData = (bodyTemp, diasPres, sysPres) => {
    if (bodyTemp !== '') {
      bodyTemp = parseFloat(bodyTemp).toFixed(2)
      
      fetch(addressInWeb + '/healthdata/', {
        method: 'POST',
        headers: {
          Accept: 'application/json',
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          owner: this.props.screenProps.userId,
          sensortype: 'Body_Temp',
          data: bodyTemp,
          date: '2018-11-07T01:59:00Z',
        }),
      })
        .then(response => response.json())
        .then(responseData => {
          console.log(
            'POST Response',
            'Response Body -> ' + JSON.stringify(responseData)
          );
        })
        .catch(error => {
          console.error(error);
        });

      if (bodyTemp > 36.9) {
        Alert.alert('Temperature of the body is high. Visit Doctor!');
      } else if(bodyTemp < 36.2) {
        Alert.alert('Temperature of the body is low. Visit Doctor!');
      }
    }

    if (diasPres !== '') {
      diasPres = parseInt(diasPres)

      fetch(addressInWeb + '/healthdata/', {
        method: 'POST',
        headers: {
          Accept: 'application/json',
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          owner: this.props.screenProps.userId,
          sensortype: 'Diastolic_Blood_Pressure',
          data: diasPres,
          date: '2018-11-07T01:59:00Z',
        }),
      })
        .then(response => response.json())
        .then(responseData => {
          console.log(
            'POST Response',
            'Response Body -> ' + JSON.stringify(responseData)
          );
        })
        .catch(error => {
          console.error(error);
        });

      if (diasPres > 90) {
        Alert.alert('Diastol Pressure is high. Visit Doctor!');
      } else if(diasPres < 60) {
        Alert.alert('Diastol Pressure is low. Visit Doctor!');
      }
    }

    if (sysPres !== '') {
      sysPres = parseInt(sysPres)

      fetch(addressInWeb + '/healthdata/', {
        method: 'POST',
        headers: {
          Accept: 'application/json',
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          owner: this.props.screenProps.userId,
          sensortype: 'Systolic_Blood_Pressure',
          data: sysPres,
          date: '2018-11-07T01:59:00Z',
        }),
      })
        .then(response => response.json())
        .then(responseData => {
          console.log(
            'POST Response',
            'Response Body -> ' + JSON.stringify(responseData)
          );
        })
        .catch(error => {
          console.error(error);
        });

      if (sysPres > 140) {
        Alert.alert('Systolic Pressure is high. Visit Doctor!');
      } else if(sysPres < 90) {
        Alert.alert('Systolic Pressure is low. Visit Doctor!');
      }
    }
    this.handleRefresh();
  };

  render() {
    if (this.state.loading === true) {
      return (
        <View style={[styles.container, styles.horizontal]}>
          <ActivityIndicator size="large" color="#0000FF" />
        </View>
      );
    } else {
      return (
        <View style={styles.first}>
          <ScrollView
            refreshControl={
              <RefreshControl
                refreshing={this.state.refreshing}
                onRefresh={this.handleRefresh}
              />
            }>
            <View style={styles.container}>
              <View style={styles.textContainer}>
                <Text style={styles.text}>
                  Current Temperature: {this.state.temp}
                </Text>
                <Text style={styles.text}>
                  Current Humidity: {this.state.humid}
                </Text>
                <Text style={styles.text}>
                  Current Gas Data: {this.state.gas}
                </Text>
              </View>

              <View style={styles.forItems}>
                <Text style={styles.titleText}>Conditioner: </Text>
                <Switch
                  onValueChange={() => this.handleCommand('Temp')}
                  value={this.state.tempTurnOnOff}
                />
              </View>
              <View style={styles.forItems}>
                <Text style={styles.titleText}>Humidifier: </Text>
                <Switch
                  onValueChange={() => this.handleCommand('Humid')}
                  value={this.state.humidTurnOnOff}
                />
              </View>
              <View style={styles.forItems}>
                <Text style={styles.titleText}>Gas leak: </Text>
                <Switch value={this.state.gasTurnOnOff} />
              </View>

              <View style={styles.forItems}>
                <Text style={styles.text}>Should Activate Conditioner: </Text>
                <Switch value={this.state.shouldActivAc} />
              </View>
              <View style={styles.forItems}>
                <Text style={styles.text}>Should Activate Humidifier: </Text>
                <Switch value={this.state.shouldActivHumid} />
              </View>

              <View style={styles.container3}>
                <Text style={styles.text}>Temperature of the body:</Text>
                <TextInput
                  autoCorrect={false}
                  style={styles.textInput}
                  autoCapitalize="none"
                  placeholder="     "
                  placeholderTextColor="#00BFFF"
                  onChangeText={bodyTemp => this.setState({ bodyTemp })}
                  value={this.state.bodyTemp}
                />
                <Text style={styles.text}>Diastolic blood pressure:</Text>
                <TextInput
                  autoCorrect={false}
                  style={styles.textInput}
                  autoCapitalize="none"
                  placeholder="     "
                  placeholderTextColor="#00BFFF"
                  onChangeText={diasPres => this.setState({ diasPres })}
                  value={this.state.diasPres}
                />
                <Text style={styles.text}>Systolic blood pressure:</Text>
                <TextInput
                  autoCorrect={false}
                  style={styles.textInput}
                  autoCapitalize="none"
                  placeholder="     "
                  placeholderTextColor="#00BFFF"
                  onChangeText={sysPres => this.setState({ sysPres })}
                  value={this.state.sysPres}
                />
                <TouchableHighlight
                  style={styles.forButton}
                  onPress={() =>
                    this.handleSaveData(
                      this.state.bodyTemp,
                      this.state.diasPres,
                      this.state.sysPres
                    )
                  }>
                  <Text style={styles.forButtonText}>Save data</Text>
                </TouchableHighlight>
              </View>
            </View>
          </ScrollView>
        </View>
      );
    }
  }
}

const styles = StyleSheet.create({
  first: {
    flex: 1,
    flexDirection: 'column',
    backgroundColor: 'white',
  },
  container3: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#00BFFF',
  },
  container: {
    flex: 1,
    backgroundColor: 'white',
    margin: 18,

    justifyContent: 'center',
    alignItems: 'center',
  },
  horizontal: {
    flexDirection: 'row',
    justifyContent: 'space-around',
    padding: 10,
  },
  forItems: {
    flexDirection: 'row',
    justifyContent: 'center',
    marginTop: 6,
    marginBottom: 6,
  },
  textContainer: {
    flex: 1,
    backgroundColor: 'white',
    marginTop: 6,

    justifyContent: 'center',
    alignItems: 'center',
  },
  titleText: {
    fontSize: 24,
    fontWeight: 'bold',
    color: 'royalblue',
  },
  text: {
    fontSize: 18,
    color: 'royalblue',
  },
  textInput: {
    fontSize: 18,
    color: '#00BFFF',
    textAlign: 'center',

    width: '80%',
    borderColor: 'white',
    backgroundColor: 'white',

    borderWidth: 1,
    borderRadius: 10,
    marginBottom: 12,
  },
  forButton: {
    height: '6%',
    justifyContent: 'center',
    alignItems: 'center',

    width: '40%',
    borderColor: '#FF9912',
    backgroundColor: '#FF9912',

    borderWidth: 1,
    borderRadius: 5,
  },
  forButtonText: {
    fontSize: 20,
    color: 'white',
    textAlign: 'center',
  },
});
