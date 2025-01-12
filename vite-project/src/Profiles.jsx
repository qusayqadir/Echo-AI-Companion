import React, { useState } from "react";
import axios from "axios";

import {
  Image,
  Box,
  Flex,
  Center,
  Heading,
  Avatar,
  Link,
  Spacer,
  Text,
  Button,
  Popover,
  PopoverTrigger,
  PopoverContent,
  PopoverHeader,
  PopoverBody,
  PopoverFooter,
  PopoverArrow,
  PopoverCloseButton,
} from "@chakra-ui/react";

import { useAuth0 } from "@auth0/auth0-react";
import About from "./About";
import { Routes, Route, Link as RouterLink, useNavigate } from "react-router-dom";

export default function Profiles() {
  const {
    loginWithRedirect,
    logout,
    isAuthenticated,
    isLoading,
    user,
    loginWithPopup,
  } = useAuth0();

  console.log("isAuthenticated:", isAuthenticated);
  console.log("isLoading:", isLoading);
  console.log("User:", user);

  const chat_id = "12345"

  // Carousel state
  const images = [
    {
      src: "char1.png",
      persona: "Persona 1",
      isEmpty: false,
    },
    {
      src: "char2.png",
      persona: "Persona 2",
      isEmpty: false,
    },
    {
      src: "char3.png",
      persona: "Persona 3",
      isEmpty: false,
    },
    {
      src: "char4.png",
      persona: "Persona 4",
      isEmpty: false,
    },
  ];
  
  const [personas, setPersonas] = useState(images);

  const toggleEmptyFlag = (index) => {
    setPersonas((prevPersonas) =>
      prevPersonas.map((persona, i) =>
        i === index
          ? { ...persona, isEmpty: !persona.isEmpty }
          : persona
      )
    );
  };  

  const [currentIndex, setCurrentIndex] = useState(0);
  const [isAnimating, setIsAnimating] = useState(false);

  const goToPrevious = () => {
    if (isAnimating) return;
    setIsAnimating(true);
    setTimeout(() => setIsAnimating(false), 500);
    setCurrentIndex((prevIndex) =>
      prevIndex === 0 ? images.length - 1 : prevIndex - 1
    );
  };

  const goToNext = () => {
    if (isAnimating) return;
    setIsAnimating(true);
    setTimeout(() => setIsAnimating(false), 500);
    setCurrentIndex((prevIndex) =>
      prevIndex === images.length - 1 ? 0 : prevIndex + 1
    );
  };

  return (
    <>
      <Flex color="gray">
        <Box />
        <Box p="6">
          <Spacer />
          <Heading>
            <Avatar boxSize="50px" name="Logo" src="echo.png" marginRight={2} />
            Echo | AI Companion
          </Heading>
        </Box>

        <Spacer />

        <Box p="10">
          <Link href="/" marginLeft={4} marginRight={4}>
            Home
          </Link>

          <Link href="/About" marginLeft={4} marginRight={4}>
            About
          </Link>

          <Link href="/FAQ" marginLeft={4} marginRight={4}>
            FAQ
          </Link>

          <Link href="/Founders" marginLeft={4} marginRight={4}>
            Founders
          </Link>

          <button
            onClick={() => {
              if (!isAuthenticated) {
                loginWithPopup();
              } else {
                logout({ returnTo: window.location.origin });
              }
            }}
          >
            {!isAuthenticated ? "Sign In" : "Log Out"}
          </button>
        </Box>
      </Flex>

      {/* Carousel with Image Buttons and Avatars */}
      <Center mt={8}>
        <Flex direction="column" align="center">
          {/* Image Display */}
          <Box
            width="400px"
            height="300px"
            overflow="hidden"
            position="relative"
          >
          <Image
            src={images[currentIndex].src}
            alt={`Slide ${currentIndex + 1}`}
            boxSize="100%"
            objectFit="cover"
            borderRadius="md"
            transition="transform 0.5s ease-in-out, opacity 0.5s ease-in-out"
            key={currentIndex}
          />
        </Box>

      <Flex mt={4} align="center" direction="column">
      {/* Persona Avatar and Details */}

  <Text mt={2} fontSize="lg" fontWeight="bold" color="gray.700">
    {personas[currentIndex].persona}
  </Text>
  
  {personas[currentIndex]?.isEmpty ? (

  <Flex>
<Text mt={2} fontSize="lg" fontWeight="bold" color="gray.700">
                <Box textAlign="center" mt={8}>
                    <Popover>
                    <PopoverTrigger>
                        <Button colorScheme="blue">New Chat</Button>
                    </PopoverTrigger>
                    <PopoverContent width="300px" height="150px">
                        <PopoverArrow />
                        <PopoverCloseButton />
                        <PopoverHeader fontWeight="bold">Upload Txt File!
                        </PopoverHeader>

                        <PopoverBody>
                        <Center marginLeft={10}>
                        <input
                                type="file"
                                onChange={(e) => {
                                    uploadImage(e);
                                }}
                                />
                        </Center>
                        </PopoverBody>
                        <PopoverFooter>
                            <Button   as={RouterLink}
    to="/Chatbot"
    onClick={() => toggleEmptyFlag(currentIndex)} >
                            </Button>
                        </PopoverFooter>
                    </PopoverContent>
                    </Popover>
                </Box>
            </Text>
          </Flex>
) : (
    <Button
    as={RouterLink}
    to="/Chatbot">
    Chat
  </Button>
)}

</Flex>

{/* Navigation Buttons */}
<Flex mt={4} justify="center" align="center" marginBottom={10}>
  <Button
    onClick={goToPrevious}
    boxSize={20}
    height={10}
    mr={1}
    _hover={{ transform: "scale(1.1)" }}
  >
    <Center>
      <Text>Previous</Text>
    </Center>
  </Button>

  <Button
    boxSize={20}
    onClick={goToNext}
    ml={1}
    height={10}
    _hover={{ transform: "scale(1.1)" }}
  >
    <Center>
      <Text>Next</Text>
    </Center>
  </Button>
</Flex>

    {!personas[currentIndex].isEmpty ? (
    <Flex>
        <Button
        onClick={async () => {
            toggleEmptyFlag(currentIndex); // Toggle the empty flag
            try {
            const chatId = personas[currentIndex].chatId || "12345"; // Default chat ID if undefined
            const response = await axios.delete(`http://127.0.0.1:5000/reset_chat/${chatId}`); // Fixed URL with template literal
            console.log(response.data.message); // Log success message
            } catch (error) {
            console.error("Error resetting chat:", error.response?.data || error.message); // Improved error handling
            }
        }}
        >
        Reset Chat
        </Button>
    </Flex>
    ) : null}

        </Flex>
      </Center>

    <Flex>
      <Spacer />
      <Box p="1" marginTop={1} ></Box>
      <Spacer />
    </Flex>

    <Flex>
        <Box marginTop='30px' bg='gray.200' w={'100%'}>
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
