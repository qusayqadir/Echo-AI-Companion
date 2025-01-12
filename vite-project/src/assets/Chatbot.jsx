import React, { useState } from "react";
import axios from "axios";
import {
  Box,
  Flex,
  Input,
  Button,
  VStack,
  HStack,
  Link
} from "@chakra-ui/react";

const Chatbot = () => {
    const [userPrompt, setUserPrompt] = useState(""); // Store the user's input
    const [conversation, setConversation] = useState([]); // Store the conversation history
    const [error, setError] = useState(""); // Store any error message
    const chatId = "12345"; // Hardcoded chat ID (replace as needed)
  
    const handleSendMessage = async () => {
      if (!userPrompt.trim()) {
        setError("Prompt is required");
        return;
      }
  
      try {
        // Make the POST request to the backend
        const response = await axios.post(`http://127.0.0.1:5000/chat/${chatId}`, {
          prompt: userPrompt,
        });
  
        // Extract the conversation from the response
        const { conversation: updatedConversation } = response.data;
  
        // Update the conversation with the new data
        setConversation(updatedConversation);
        setUserPrompt(""); // Clear input field
        setError(""); // Clear any error message
      } catch (err) {
        // Handle errors
        if (err.response) {
          setError(err.response.data.error || "An error occurred");
        } else {
          setError("Network error");
        }
      }
    };
  
    return (
    <>
    <Flex>
        <Link href="/Profiles" marginLeft={4} marginRight={4}>
        Founders
        </Link>
    </Flex>

      <Flex direction="column" height="100vh">
        {/* Chat Display */}
        <VStack
          flex="1"
          overflowY="auto"
          spacing={4}
          bg="gray.100"
          p={4}
          align="stretch"
        >
          {conversation.map((message, index) => (
            <Box
              key={index}
              alignSelf={message.role === "user" ? "flex-end" : "flex-start"}
              bg={message.role === "user" ? "blue.500" : "gray.300"}
              color={message.role === "user" ? "white" : "black"}
              p={3}
              borderRadius="lg"
              maxWidth="75%"
            >
              {message.content}
            </Box>
          ))}
        </VStack>
  
        {/* Input Section */}
        <HStack p={4} bg="white" borderTop="1px solid #e2e8f0">
          <Input
            placeholder="Type your message..."
            value={userPrompt}
            onChange={(e) => setUserPrompt(e.target.value)}
            onKeyDown={(e) => e.key === "Enter" && handleSendMessage()}
          />
          <Button onClick={handleSendMessage} colorScheme="blue">
            Send
          </Button>
        </HStack>
        {error && (
          <Box p={2} bg="red.300" color="white" textAlign="center">
            {error}
          </Box>
        )}
      </Flex>
    </>
    );
  };

export default Chatbot;
