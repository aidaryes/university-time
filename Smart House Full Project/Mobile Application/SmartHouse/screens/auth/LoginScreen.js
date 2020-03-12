import React from 'react';
import {
  StyleSheet,
  TextInput,
  View,
  Alert,
  Button,
  Text,
  TouchableHighlight,
} from 'react-native';

var addressInWeb = 'http://68.183.214.100:8080';

export default class LoginScreen extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      email: '',
      password: '',

      allUsers: [],
    };
  }

  componentDidMount() {
    this.loadUsers();
  }

  loadUsers = () => {
    fetch(addressInWeb + '/users/')
      .then(response => response.json())
      .then(allUsers => {
        this.setState({
          allUsers: allUsers,
        });
      })
      .catch(error => {
        console.error(error);
      });
  };

  handleLogin = (email, password) => {
    var didExist = 0;
    for (var i = 0; i < this.state.allUsers.length; i++) {
      if (email === this.state.allUsers[i].email) {
        didExist = 1;
        if (password === this.state.allUsers[i].password) {
          this.props.navigation.navigate('Main', {
            userId: this.state.allUsers[i].id,
          });
        } else {
          Alert.alert('Incorrect Password. Please, try again.');
        }
      }
    }
    if (didExist == 0) {
      Alert.alert('Email is invalid. Please, try again.');
    }
  };

  render() {
    return (
      <View style={styles.container}>
        <Text style={styles.text}>Login</Text>
        <TextInput
          autoCorrect={false}
          style={styles.textInput}
          autoCapitalize="none"
          placeholder="Email"
          placeholderTextColor="#00BFFF"
          onChangeText={email => this.setState({ email })}
          value={this.state.email}
        />
        <TextInput
          autoCorrect={false}
          secureTextEntry
          style={styles.textInput}
          autoCapitalize="none"
          placeholder="Password"
          placeholderTextColor="#00BFFF"
          onChangeText={password => this.setState({ password })}
          value={this.state.password}
        />
        <TouchableHighlight
          style={styles.forButton}
          onPress={() =>
            this.handleLogin(this.state.email, this.state.password)
          }>
          <Text style={styles.forButtonText}>Sign In</Text>
        </TouchableHighlight>
      </View>
    );
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#00BFFF',
  },
  text: {
    fontWeight: 'bold',
    fontSize: 24,
    marginBottom: 12,
    color: 'white',
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
