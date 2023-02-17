import { StyleSheet, View, Pressable, Text } from 'react-native';
import FontAwesome from "@expo/vector-icons/FontAwesome";


async function sendDataToFirebase(data) {
    try {
      const timestamp = Math.floor(Date.now() / 1000);
      console.log(timestamp)

      const response = await fetch(`https://wiseblinds-default-rtdb.europe-west1.firebasedatabase.app/mannual/${timestamp}.json`, {
        method: "PUT",
        body: JSON.stringify(data)
      });
      const responseJson = await response.json();
      console.log(responseJson);
    } catch (error) {
      console.error(error);
    }
  }

  async function sendVoiceDataToFirebase(data) {
    try {
      const timestamp = Math.floor(Date.now() / 1000);
      console.log(timestamp)

      const response = await fetch(`https://wiseblinds-default-rtdb.europe-west1.firebasedatabase.app/voice/${timestamp}.json`, {
        method: "PUT",
        body: JSON.stringify(data)
      });
      const responseJson = await response.json();
      console.log(responseJson);
    } catch (error) {
      console.error(error);
    }
  }



export default function Button({ label, theme, data, id }) {
  if (theme === "manual") {
    return (
      <View style={[styles.buttonContainer, { marginTop: 10}]}>
        <Pressable
          style={[styles.button, { backgroundColor: 'transparent' }]}
          onPress={() => {
            console.log("zack smells very good")
            sendDataToFirebase({
              ID: id,
              position: data,
          });
        }}
        >
          <Text style={[styles.buttonLabel, { color: "white" }]}>{label}</Text>
        </Pressable>
    </View>
    );
  }
  if (theme === "voicecontrol") {
    return (
      <View style={[styles.buttonSecondContainer, { marginTop: 10 }]}>
        <Pressable
          style={[styles.button, { backgroundColor: 'transparent' }]}
          onPress={() => {
            console.log("zack smells very not disabled")
            sendVoiceDataToFirebase({
            ID: id,
            disabled: data,
          });
        }}
        >
          <Text style={[styles.buttonLabel, { color: "white" }]}>{label}</Text>
        </Pressable>
    </View>
    );
  }
}

const styles = StyleSheet.create({
  buttonSecondContainer: {
    width: 150,
    height: 60,
    marginHorizontal: 20,
    marginVertical: 0,
    alignItems: 'center',
    justifyContent: 'center',
    padding: 0,
    backgroundColor: 'transparent',
    color: 'white',
  },

  buttonContainer: {
    width: 150,
    height: 60,
    marginHorizontal: 20,
    marginVertical: 0,
    alignItems: 'center',
    justifyContent: 'center',
    padding: 0,
    backgroundColor: 'transparent',
    color: 'white',
  },
  button: {
    borderWidth: 5,
    borderColor: "#808080",
    borderRadius: 10,
    width: '100%',
    height: '100%',
    alignItems: 'center',
    justifyContent: 'center',
    flexDirection: 'row',
    color: 'white',
  },
  buttonLabel: {
    color: '#FFFFFF',
    fontSize: 20,

  },
});
