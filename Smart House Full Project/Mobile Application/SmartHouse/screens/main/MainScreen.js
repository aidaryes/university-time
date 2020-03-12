import React from 'react';
import { createBottomTabNavigator } from 'react-navigation';

import ControlPanel from './ControlPanelScreen';
import PersonalInfo from './PersonalInfoScreen';
import ViewData from './ViewDataScreen';

const AppNavigator = createBottomTabNavigator(
  {
    PersonalInfo,
    ViewData,
    ControlPanel,
  },
  {
    initialRouteName: 'PersonalInfo',
    
    tabBarOptions: {
      activeBackgroundColor: '#FF9912',
      inactiveBackgroundColor: 'royalblue',   
      showIcon: true,
      
      labelStyle: {
        fontSize: 12,
        color: 'white',
      },
    },
  }
);

class Main extends React.Component {
  render() {
    const screenProps = {
      userId: this.props.navigation.state.params.userId,
    };

    return <AppNavigator screenProps={screenProps} />;
  }
}

export default Main;