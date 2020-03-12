import React from 'react';
import { StyleSheet, View, Text } from 'react-native';

export default class LoadingScreen extends React.Component {
  componentDidMount() {
    setTimeout(() => {
      this.props.navigation.navigate('Login');
    }, 3000);
  }

  render() {
    return (
      <View style={styles.container}>
        <Text style={styles.text}>Smart House Project</Text>
      </View>
    );
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#FF9912',
  },
  text: {
    fontSize: 24,
    color: 'white',
    textAlign: 'center',
  },
});
