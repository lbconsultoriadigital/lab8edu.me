import Anthropic from '@anthropic-ai/sdk';
import dotenv from 'dotenv';

dotenv.config();

const apiKey = process.env.ANTHROPIC_API_KEY;

if (!apiKey) {
  console.error("Error: ANTHROPIC_API_KEY is not set in environment variables.");
  process.exit(1);
}

const anthropic = new Anthropic({ apiKey });

async function main() {
  console.log("Sending request to Claude 3.5 Sonnet...");

  try {
    const stream = await anthropic.messages.create({
      model: "claude-3-5-sonnet-20241022",
      max_tokens: 1024,
      system: "You are a helpful and concise AI assistant developed by Anthropic.",
      messages: [
        {
          role: "user",
          content: "Explain in two concise paragraphs how Model Context Protocol (MCP) works and why it matters for developers."
        }
      ],
      stream: true,
    });

    for await (const chunk of stream) {
      if (chunk.type === "content_block_delta" && chunk.delta?.text) {
        process.stdout.write(chunk.delta.text);
      }
    }
    console.log("\n\nDone!");
  } catch (error) {
    console.error("API request failed:", error.message);
  }
}

main();
