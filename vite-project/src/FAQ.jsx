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
  useColorModeValue,
  Container,
  Accordion,
  AccordionItem,
  AccordionButton,
  AccordionPanel,
  Stack,

} from "@chakra-ui/react";


import { ChevronDownIcon } from '@chakra-ui/icons'
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
          <Avatar boxSize="50px" name="Logo" src="echo.png" marginRight={2}/>
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
            Frequently Asked Questions
          </Heading>
        </Center>
      </Box>

      <Spacer>

      <Box marginTop={'50px'} p="4" mx="auto" maxW="4xl" bg="gray.100" borderRadius="md">

        <Text fontSize="lg" mb="4">
        Welcome to our FAQ section! Here, you'll find answers to the most common questions
         about using our site, interacting with the chatbot, and customizing your experience. 
         Whether you're curious about how the platform works, need help troubleshooting an issue, 
         or want to learn about the features we offer, this is the place to start. If you don’t see your 
         question here, feel free to reach out to us directly—we’re here to help!
        </Text>
      </Box>

      </Spacer> 

      <Flex
      minH={'65vh'}
      justify={'center'}
      bg={useColorModeValue('white')}>
      <Container>
        <Accordion marginBottom='20' marginTop='100' allowMultiple width="100%" maxW="lg" rounded="lg">
          <AccordionItem>
          <AccordionButton
              display="flex"
              alignItems="center"
              justifyContent="space-between"
              p={4}>
              <Text fontSize="md">What is Echo AI?</Text>
              <ChevronDownIcon fontSize="24px" />
            </AccordionButton>
            <AccordionPanel pb={4}>
              <Text color="gray.600">
              Echo AI is an advanced chatbot platform designed to emulate the texting styles of specific 
              personas. It uses state-of-the-art artificial intelligence models to provide tailored, dynamic, 
              and engaging conversations that adapt to your input. Whether you're seeking assistance, entertainment, 
              or learning, Echo AI offers a unique interactive experience.
              </Text>
            </AccordionPanel>
          </AccordionItem>
          <AccordionItem>
          <AccordionButton
              display="flex"
              alignItems="center"
              justifyContent="space-between"
              p={4}>
              <Text fontSize="md">How do I begin a conversation?</Text>
              <ChevronDownIcon fontSize="24px" />
            </AccordionButton>
            <AccordionPanel pb={4}>
              <Text color="gray.600">
              To begin a conversation, select a persona from the available options. 
              If the persona has no active chat history, click the "New Chat" button to 
              start fresh. For personas with existing conversations, you can continue 
              where you left off or reset the chat history before starting over.
              </Text>
            </AccordionPanel>
          </AccordionItem>
          <AccordionItem>
            <AccordionButton
              display="flex"
              alignItems="center"
              justifyContent="space-between"
              p={4}>
              <Text fontSize="md">Can I use multiple personas in one session?</Text>
              <ChevronDownIcon fontSize="24px" />
            </AccordionButton>
            <AccordionPanel pb={4}>
              <Text color="gray.600">
              Yes, you can interact with multiple personas in the same session. Each 
              persona maintains its unique conversation history, allowing you to switch 
              between them seamlessly. Simply select a persona and begin chatting.
              </Text>
            </AccordionPanel>
          </AccordionItem>
          <AccordionItem>
            <AccordionButton
              display="flex"
              alignItems="center"
              justifyContent="space-between"
              p={4}>
              <Text fontSize="md">Is my data secure?</Text>
              <ChevronDownIcon fontSize="24px" />
            </AccordionButton>
            <AccordionPanel pb={4}>
              <Text color="gray.600">
              Yes, your data is secure. Echo AI prioritizes your privacy by 
              storing conversations locally in your browser unless you log in 
              and choose to sync them. Uploaded files are processed temporarily 
              and not stored permanently unless explicitly agreed upon. We implement 
              strong security measures to protect your information.
                </Text>
            </AccordionPanel>
          </AccordionItem>
          <AccordionItem>
            <AccordionButton
              display="flex"
              alignItems="center"
              justifyContent="space-between"
              p={4}>
              <Text fontSize="md">How can I contribute to the development of Echo?</Text>
              <ChevronDownIcon fontSize="24px" />
            </AccordionButton>
            <AccordionPanel pb={4}>
              <Text color="gray.600">
              We welcome contributions to the development of Echo AI! Visit our GitHub 
              repository to explore the codebase, suggest improvements, or submit feature 
              requests. For collaboration opportunities or inquiries, feel free to contact our 
              development team via the "Contact Us" section on the website. Your input is valued 
              and helps shape Echo AI's future!
                </Text>
            </AccordionPanel>
          </AccordionItem>
        </Accordion>
      </Container>
    </Flex>

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