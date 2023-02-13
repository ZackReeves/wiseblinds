import { StyleSheet, ImageBackground } from 'react-native';

export default function ImageViewer({ placeholderImageSource }) {
  return (
    <ImageBackground source={placeholderImageSource} style={styles.image} resizeMode="cover"/>
  );
}

const styles = StyleSheet.create({
  image: {
    flex: 1,
    justifyContent: 'center',
  },
});
