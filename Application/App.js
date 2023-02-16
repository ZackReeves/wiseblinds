import { StatusBar } from 'expo-status-bar';
import React, {useState, useEffect} from 'react';
import {SafeAreaView, Switch, View, Text, ImageBackground, StyleSheet, Image, TouchableOpacity} from 'react-native';

import Button from './components/Button';

const BackgroundImage = require('./assets/background.jpg');
const LogoImage = require('./assets/logo.png');

// ---------------------------get_temp_data_from_firebase------------------------

async function fetchTemperatureData() {
  var now = Math.floor(Date.now() / 1000);  

  var url = `https://wiseblinds-default-rtdb.europe-west1.firebasedatabase.app/temp_rh.json?orderBy="$key"&startAt="${now-60}"&endAt="${now}"`;
  
  try {
    const response = await fetch(url);
    const responseJson = await response.json();
    //console.log(responseJson)

    let temp = 0;
    let rh = 0;
    let count = 0;
    for (let i in responseJson){
      temp+= responseJson[i]['temp'];
      rh += responseJson[i]['rh'];
      count++;
    }

    temp /= count;
    rh /= count;

    return [temp, rh];
  } catch (error) {
    console.error(error);
  }
}
//-----------------------------------Switch-----------------------------------------------------------
const App = () => {

  
  const [temperature, setTemperature] = useState(null);
  const [humidity, setHumidity] = useState(null);
  const [isOn, setIsOn] = useState(false);
  const[previousState, setSwitchValue] = useState(false)
  // const [accessToken, setAccessToken] = useState(Null);
  
  const toggleSwitch = () => setSwitchValue(previousState => !previousState)
  
  


  useEffect(() => {

    // var {google} = require("googleapis");

    // var serviceAccount = require("./wiseblinds-firebase-adminsdk-pkvk1-ad89d55f1f.json")

    // var scopes = [
    //   "https://www.googleapis.com/auth/userinfo.email",
    //   "https://www.googleapis.com/auth/firebase.database"
    // ];

    // var jwtClient = new google.auth.JWT(
    //   serviceAccount.client_email,
    //   null,
    //   serviceAccount.private_key,
    //   scopes
    // );

    // jwtClient.authorize(function(error, tokens) {
    //   setAccessToken(tokens.access_token);
    // });

    const intervalId = setInterval(() => {
      fetchTemperatureData().then(data => {
        setTemperature(data[0]);
        setHumidity(data[1]);
      });
    }, 1200); // 2 minutes = 120 seconds = 120000 milliseconds

    return () => clearInterval(intervalId);
  }, []);
  

  return (
    
    <SafeAreaView style={styles.container}>
      <ImageBackground source={BackgroundImage} style={styles.backgroundstyle} resizeMode="cover">
      <View style={styles.logoContainer}>
    <Image source={LogoImage} style={styles.logo} />
  </View>
        <View>
          <View>
            <Text style={styles.titleStyle}>Temperature: {Math.round(temperature, 2)}</Text>
            <Text style={styles.titleStyle}>Humidity: {Math.round(humidity, 2)}</Text>
          </View>
        </View>

        <View style={styles.footerContainer}>
          <Button theme="manual" label="Open" data='1' />
          <Button theme="manual" label="Close" data='0' />
          <Button theme="manual" label="Automatic" data='2' />
          <TouchableOpacity onPress={toggleSwitch} style={isOn ? styles.buttonOn : styles.buttonOff}>
            <Button  theme="voicecontrol" label = "Voice Control" data ={previousState}/>
          </TouchableOpacity> 
        </View>
      <StatusBar style="auto" />
      </ImageBackground>
    </SafeAreaView>

  );
};
export default App;
const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  buttonOn: {
    width: 150,
    height: 60,
    backgroundColor: 'transparent',
    borderRadius: 100,
    marginHorizontal: 20,
    marginVertical: 20,
    padding: 0,
    alignItems: 'center',
    justifyContent: 'center',
  },
  buttonOff: {
    width: 150,
    height: 40,
    backgroundColor: 'transparent',
    borderRadius: 100,
    marginHorizontal: 20,
    marginVertical: 20,
    padding: 0,
    alignItems: 'center',
    justifyContent: 'center',
  },
  buttonText: {
    color: 'white',
    fontSize: 20,
    fontWeight: 'bold',
  },

  headerText: {
    fontSize: 50,
    fontWeight: 'bold',
    textAlign: 'center',
    color: 'white',
  },
  backgroundstyle: {
    flex: 1,
    justifyContent: 'center',
  },
  imageContainer: {
    flex: 1,
    paddingTop: 10,
    justifyContent: 'center',
  },
  titleStyle: {
    fontSize: 20,
    fontWeight: 'bold',
    textAlign: 'left',
    padding: 10,
    color: 'white',
  },

  footerContainer: {
    flex: 1/3,
    alignItems: 'center',
    backgroundColor: '#transparent',
    color: 'white',
  },
  logoContainer: {
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: 'transparent',
    paddingBottom: 20,
  },
  logo: {
    width: 200,
    height: 200,
  },

});
