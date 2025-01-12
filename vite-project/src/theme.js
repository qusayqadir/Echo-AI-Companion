import { extendTheme } from "@chakra-ui/react";

const theme = extendTheme({
  styles: {
    global: {
      body: {
        bg: "yellow.40", // Dark gray background
        color: "black", // White font color
      },
    },
  },
});

export default theme;
