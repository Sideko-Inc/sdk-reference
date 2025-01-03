import fs from "fs";
import Client, { Environment } from "my_petstore_ts";

describe("tests client.pet.image.upload", () => {
  test.concurrent(
    "POST /pet/{petId}/uploadImage | testId: success_default | Success test with response schema validation. Expects status code 200",
    async () => {
      const client = new Client({
        apiKey: "API_KEY",
        oauthToken: "API_TOKEN",
        environment: Environment.MockServer,
      });
      const uploadFile = fs.createReadStream("uploads/file.pdf");
      // Get both raw response for status and parsed response for data
      const [rawResponse, response] = await Promise.all([
        client.pet.image.upload({ data: uploadFile, petId: 123 }).asResponse(),
        client.pet.image.upload({ data: uploadFile, petId: 123 }),
      ]);
      expect(rawResponse.status).toBe(200); // Exact status code match
      // Response body automatically validated by Zod schema during deserialization
      expect(response).toBeDefined();
    },
  );
});
