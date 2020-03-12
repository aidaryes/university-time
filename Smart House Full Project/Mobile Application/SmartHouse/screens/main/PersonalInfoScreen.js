import React from 'react';
import {
  View,
  Text,
  StyleSheet,
  Alert,
  ActivityIndicator,
  ScrollView,
  RefreshControl,
  Image,
  FlatList,
  TouchableHighlight,
  Switch,
} from 'react-native';
import { List } from 'react-native-elements';

var addressInWeb = 'http://68.183.214.100:8080';

export default class PersonalInfo extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      ageCateg: false,
      disCateg: false,

      userData: [],
      
      visitors: [],
      visitor: '',

      dataWithPhotos: [],

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
      addressInWeb + '/users/' + this.props.screenProps.userId + '/'
    )
      .then(response => response.json())
      .then(userData => {
        this.setState({
          userData: userData,
        });
      })
      .catch(error => {
        console.error(error);
      });

    await fetch(addressInWeb + '/photos/' + this.props.screenProps.userId + '/')
      .then(response => response.json())
      .then(dataWithPhotos => {
        this.setState({
          dataWithPhotos: dataWithPhotos,
        });
      })
      .catch(error => {
        console.error(error);
      });

    await fetch(addressInWeb + '/visitors/' + this.props.screenProps.userId + '/')
      .then(response => response.json())
      .then(visitors => {
        this.setState({
          visitors: visitors,
        });
      })
      .catch(error => {
        console.error(error);
      });

    var visitSize = this.state.visitors.length;
    if(visitSize !== 0) {
      var visitorLast = this.state.visitors[visitSize - 1].who;
      Alert.alert('Detected known person. ', visitorLast);

      this.setState({
        visitor: visitorLast,
      });
    } else {
      this.setState({
        visitor: '',
      });
    }   

    var age = this.state.userData[0].ageCategory;
    var disease = this.state.userData[0].diseaseCategory;
    if(age === 0) {
      age = false
    } else if(age === 1) {
      age = true
    } else {
      console.log("Age problems")
    }

    if(disease === 0) {
      disease = false
    } else if(disease === 1) {
      disease = true
    } else {
      console.log("Disease problems")
    }

    this.setState({
      ageCateg: age,
      disCateg: disease,
    });

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

  handleAccept = fotoid => {
    fetch(addressInWeb + '/photos/accepted/' + fotoid + '/')
      .then(response => response.json())
      .then(() => {
        this.handleRefresh();
      })
      .catch(error => {
        console.error(error);
      });
  };

  handleCallPolice = () => {
    Alert.alert('Detected unknown person. Call to Police!!!');
  };

  postMethodAge = status => {
    fetch(addressInWeb + '/users/' + this.props.screenProps.userId + '/changeAgeCategoryData/', {
      method: 'POST',
      headers: {
        Accept: 'application/json',
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        fromuser: this.props.screenProps.userId,
        ageCategory: status,
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

  postMethodDis = status => {
    fetch(addressInWeb + '/users/' + this.props.screenProps.userId + '/changeDiseaseCategoryData/', {
      method: 'POST',
      headers: {
        Accept: 'application/json',
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        fromuser: this.props.screenProps.userId,
        diseaseCategory: status,
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
    if (command === 'Age') {
      if (this.state.ageCateg === false) {
        this.postMethodAge(1);
        this.setState({
          ageCateg: true,
        });
      } else if(this.state.ageCateg === true) {
        this.postMethodAge(0);
        this.setState({
          ageCateg: false,
        });
      }
    }
    if (command === 'Disease') {
      if (this.state.disCateg === false) {
        this.postMethodDis(1);
        this.setState({
          disCateg: true,
        });
      } else if(this.state.disCateg === true) {
        this.postMethodDis(0);
        this.setState({
          disCateg: false,
        });
      }
    }
  }

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
                <Text style={styles.text}>Welcome</Text>
                <View style={styles.forItems}>
                  <Text style={styles.text}>Are you above 50?: </Text>
                  <Switch
                    onValueChange={() => this.handleCommand('Age')}
                    value={this.state.ageCateg}
                  />
                </View>
                <View style={styles.forItems}>
                  <Text style={styles.text}>Do you have problems with health?: </Text>
                  <Switch
                    onValueChange={() => this.handleCommand('Disease')}
                    value={this.state.disCateg}
                  />
                </View>
                <Text style={styles.text}>Visitor: {this.state.visitor}</Text>
              </View>

              <View style={styles.listContainer}>
                <List containerStyle={styles.listDesign}>
                  <FlatList
                    data={this.state.dataWithPhotos}
                    keyExtractor={item => item.id.toString()}
                    renderItem={({ item }) => (
                      <View style={styles.betweenPhoto}>
                        <Image
                          source={{
                            uri: addressInWeb + '/' + item.photo,
                          }}
                          style={{ width: 250, height: 250 }}
                        />
                        <View style={styles.betweenButtons}>
                          <TouchableHighlight
                            style={styles.forButton}
                            onPress={() => this.handleAccept(item.id)}>
                            <Text style={styles.forButtonText}>Accept</Text>
                          </TouchableHighlight>
                          <TouchableHighlight
                            style={styles.forButton}
                            onPress={() => this.handleCallPolice()}>
                            <Text style={styles.forButtonText}>102</Text>
                          </TouchableHighlight>
                        </View>
                      </View>
                    )}
                  />
                </List>
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
  container: {
    flex: 1,
    backgroundColor: 'white',
    margin: 18,

    justifyContent: 'center',
    alignItems: 'center',
  },
  textContainer: {
    flex: 1,
    backgroundColor: 'white',
    margin: 6,

    justifyContent: 'center',
    alignItems: 'center',
  },
  listContainer: {
    flex: 1,
    backgroundColor: 'white',
  },
  betweenPhoto: {
    margin: 6,
  },
  listDesign: {
    backgroundColor: 'white',

    alignItems: 'center',
    borderTopWidth: 0,
    borderBottomWidth: 0,
  },
  betweenButtons: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    margin: 6,
  },
  forButton: {
    flex: 1,
    marginLeft: 6,
    marginRight: 6,

    height: 'auto',
    justifyContent: 'center',
    alignItems: 'center',

    borderColor: 'royalblue',
    backgroundColor: 'royalblue',

    borderWidth: 1,
    borderRadius: 5,
  },
  text: {
    fontSize: 18,
    color: 'royalblue',
  },
  forButtonText: {
    fontSize: 20,
    color: 'white',
    textAlign: 'center',
  },
  forItems: {
    flexDirection: 'row',
    justifyContent: 'center',
    marginTop: 6,
    marginBottom: 6,
  },
});
