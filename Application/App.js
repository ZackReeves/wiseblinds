import { StatusBar } from 'expo-status-bar';
import React, {useState, useEffect} from 'react';
import {SafeAreaView, View, Text, ImageBackground, StyleSheet, Image,} from 'react-native';


import Button from './components/Button';


const BackgroundImage = require('./assets/background.jpg');

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

const App = () => {

  const [temperature, setTemperature] = useState(null);
  const [humidity, setHumidity] = useState(null);

  useEffect(() => {
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
        <View>
          <View style={styles.headerContainer}>
            <Text style={styles.headerText}>WiseBlinds</Text>
          <View>
          </View>
            <Text style={styles.titleStyle}>Temperature: {Math.round(temperature, 1)}</Text>
            <Text style={styles.titleStyle}>Humidity: {Math.round(humidity, 1)}</Text>
          </View>
        </View>

        <View style={styles.footerContainer}>
          <Button theme="primary" label="Open" data='1' />
          <Button theme="primary" label="Close" data='0' />
          <Button theme="primary" label="Automatic" data='2' />
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
  headerContainer: {
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: 'transparent',
  },
  headerText: {
    fontSize: 50,
    fontWeight: 'bold',
    fontFamily: 'TTR',
    textAlign: 'center',
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
    fontSize: 28,
    fontWeight: 'bold',
    textAlign: 'left',
    padding: 10,
  },

  footerContainer: {
    flex: 1/3,
    alignItems: 'center',
    backgroundColor: '#0000',
  },

});
