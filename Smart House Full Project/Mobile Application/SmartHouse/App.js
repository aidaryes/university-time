import { createSwitchNavigator } from 'react-navigation';

import Loading from './screens/auth/LoadingScreen';
import Login from './screens/auth/LoginScreen';
import Main from './screens/main/MainScreen';

const App = createSwitchNavigator(
  {
    Loading,
    Login,
    Main,
  },
  {
    initialRouteName: 'Loading',
  }
);

export default App;
