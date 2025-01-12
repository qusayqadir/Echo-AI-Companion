

import React from "react";
import {
  Image,
  Box,
  Text,
  Spacer,
  Flex,
  Button,
  Center,
  Heading,
  Avatar,
  Link,
} from "@chakra-ui/react";

import { useAuth0 } from "@auth0/auth0-react";

export default function FAQ() {

    const { loginWithRedirect, logout, isAuthenticated, isLoading, user, loginWithPopup } = useAuth0();

    console.log("isAuthenticated:", isAuthenticated);
    console.log("isLoading:", isLoading);
    console.log("User:", user);
  return (
    <>
    <Flex color="gray">
      <Box />
      <Box p="6">
        <Spacer />
        <Heading>
          <Avatar boxSize="50px" name="Logo" src="echo.png" />
          Echo | AI Companion 
        </Heading>
      </Box>
      
      <Spacer />

      <Box p="10">

          <Link href = "/" marginLeft={4} marginRight={4}>
            Home
          </Link>

          <Link href = "/About" marginLeft={4} marginRight={4}>
            About
          </Link>

          <Link href = "/FAQ" marginLeft={4} marginRight={4}>
            FAQ
          </Link>

          <Link href = "/Founders" marginLeft={4} marginRight={4}>
            Founders
          </Link>

        <Button
          onClick={() => {
            if (!isAuthenticated) {
              loginWithPopup();
            } else {
              logout({ returnTo: window.location.origin });
            }
          }}
          colorScheme="gray"
        >
          {!isAuthenticated ? 'Sign In' : 'Log Out'}
        </Button>

      </Box>
    </Flex>

      <Box bg = 'white' p="6" mx="auto">
        <Center>
          <Heading as="h2" size="xl" mb="4">
            About Echo AI
          </Heading>
        </Center>
      </Box>

      <Box p="4" mx="auto" maxW="4xl">
        <Text fontSize="lg" mb="4">
          meow
        </Text>
      </Box>

      <Box p="4" mx="auto" maxW="4xl" bg='white' borderRadius="md">
        <Heading as="h3" size="lg" mb="2">
          Our Story
        </Heading>
        <Text fontSize="lg" mb="4">
          meow
        </Text>
      </Box>

      <Box p="4" mx="auto" maxW="4xl">
        <Heading as="h3" size="lg" mb="2">
          What We Offer
        </Heading>
        <Text fontSize="lg" mb="2">
          <strong>Smart Waste Identification:</strong> Simply take a picture of your trash using the SnapWaste app or website. Our advanced AI technology analyzes the image and identifies whether the item should be recycled, composted, or sent to the landfill.
        </Text>
        <Text fontSize="lg" mb="2">
          <strong>Personalized Disposal Instructions:</strong> SnapWaste doesn’t just tell you where to dispose of your waste; it also provides detailed instructions on how to prepare items for disposal. This includes steps like cleaning or rinsing containers before recycling them, ensuring that you follow the best practices for waste management.
        </Text>
        <Text fontSize="lg" mb="2">
          <strong>Locate Disposal Centers:</strong> Our platform helps you find the nearest recycling centers, compost facilities, and garbage disposal sites. Whether you're at home or traveling, SnapWaste ensures you can easily locate a facility to drop off your waste.
        </Text>
      </Box>

      <Box p="4" mx="auto" maxW="4xl" bg="gray.100" borderRadius="md">
        <Heading as="h3" size="lg" mb="2">
          Why Choose SnapWaste?
        </Heading>
        <Text fontSize="lg" mb="2">
          <strong>Easy to Use:</strong> Our intuitive interface makes waste management simple. Just snap a picture, and let SnapWaste guide you through the rest.
        </Text>
        <Text fontSize="lg" mb="2">
          <strong>Educational Resources:</strong> SnapWaste offers a wealth of information on waste reduction, recycling best practices, and sustainable living tips. We aim to educate and empower our users to make environmentally-friendly choices.
        </Text>
        <Text fontSize="lg" mb="2">
          <strong>Community Engagement:</strong> Join a community of environmentally conscious individuals dedicated to reducing waste and promoting sustainability. Share tips, ask questions, and learn from others.
        </Text>
        <Text fontSize="lg" mb="2">
          <strong>Continuous Innovation:</strong> We are committed to continuously improving our technology and expanding our database to provide the most accurate and helpful information. Your feedback is essential in helping us enhance our services.
        </Text>
      </Box>

      <Box p="4" mx="auto" maxW="4xl">
        <Text fontSize="lg" mb="4">
          At SnapWaste, we believe that proper waste management is crucial for a sustainable future. Join us in making a positive impact on our environment by disposing of waste the right way, one snap at a time.
        </Text>
      </Box>

    <Flex>
        <Box marginBottom='-33px' bg='gray.200' w={'100%'}>
          <Center>
            <Text marginTop='1' marginRight={5}>
              Privacy Policy and Terms of Service
              </Text>
            </Center>
          </Box>
        </Flex>
    </>
  );
}