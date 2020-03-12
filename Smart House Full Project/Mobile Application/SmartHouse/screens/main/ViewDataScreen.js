import React from 'react';
import {
  View,
  Text,
  StyleSheet,
  ActivityIndicator,
  ScrollView,
  RefreshControl,
} from 'react-native';
import { LineChart, YAxis, Grid } from 'react-native-svg-charts';

var addressInWeb = 'http://68.183.214.100:8080';

export default class ViewData extends React.PureComponent {
  constructor(props) {
    super(props);

    this.state = {
      dataForTemp: [],
      dataForHumid: [],

      arrayTemp: [],
      arrayHumid: [],

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

    this.setState({
      arrayTemp: [],
      arrayHumid: [],
    });

    //Delete first 4 data
    for (var i = 4; i < this.state.dataForTemp.length; i++) {
      await this.setState({
        arrayTemp: [...this.state.arrayTemp, this.state.dataForTemp[i].data],
      });
    }

    for (i = 0; i < this.state.dataForHumid.length; i++) {
      await this.setState({
        arrayHumid: [...this.state.arrayHumid, this.state.dataForHumid[i].data],
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

  render() {
    const contentInset = { top: 20, bottom: 20 };

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
                <Text style={styles.text}>Temperature Graph:</Text>
                <View style={{ height: 200, flexDirection: 'row' }}>
                  <YAxis
                    data={this.state.arrayTemp}
                    contentInset={contentInset}
                    svg={{
                      fill: 'grey',
                      fontSize: 10,
                    }}
                    numberOfTicks={10}
                    formatLabel={value => `${value}ºC`}
                  />
                  <LineChart
                    style={{ flex: 1, marginLeft: 16 }}
                    data={this.state.arrayTemp}
                    svg={{ stroke: 'rgb(134, 65, 244)' }}
                    contentInset={contentInset}>
                    <Grid />
                  </LineChart>
                </View>
              </View>
              <View style={styles.textContainer}>
                <Text style={styles.text}>Humidity Graph:</Text>
                <View style={{ height: 200, flexDirection: 'row' }}>
                  <YAxis
                    data={this.state.arrayHumid}
                    contentInset={contentInset}
                    svg={{
                      fill: 'grey',
                      fontSize: 10,
                    }}
                    numberOfTicks={10}
                    formatLabel={value => `${value}%`}
                  />
                  <LineChart
                    style={{ flex: 1, marginLeft: 16 }}
                    data={this.state.arrayHumid}
                    svg={{ stroke: 'rgb(134, 65, 244)' }}
                    contentInset={contentInset}>
                    <Grid />
                  </LineChart>
                </View>
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
  horizontal: {
    flexDirection: 'row',
    justifyContent: 'space-around',
    padding: 10,
  },
  textContainer: {
    flex: 1,
    backgroundColor: 'white',
    margin: 6,

    justifyContent: 'center',
    alignItems: 'center',
  },
  text: {
    fontSize: 18,
    color: 'royalblue',
  },
});
