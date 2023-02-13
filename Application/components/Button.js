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



export default function Button({ label, theme, data }) {
  if (theme === "primary") {
    return (
      <View style={[styles.buttonContainer, { marginTop: 75 }]}>
        <Pressable
          style={[styles.button, { backgroundColor: 'transparent' }]}
          onPress={() => {
            console.log("zack smells very good")
            sendDataToFirebase({
            position: data,
          });
        }}
        >
          <Text style={[styles.buttonLabel, { color: "#25292e" }]}>{label}</Text>
        </Pressable>
    </View>
    );
  }
}

const styles = StyleSheet.create({
  buttonContainer: {
    width: 150,
    height: 60,
    marginHorizontal: 20,
    marginVertical: 0,
    alignItems: 'center',
    justifyContent: 'center',
    padding: 0,
    backgroundColor: 'transparent',
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
  },
  buttonLabel: {
    color: '#25292e',
    fontSize: 20,
  },
});