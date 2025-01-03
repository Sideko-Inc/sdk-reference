import Client, { Environment } from "my_petstore_ts";

describe("tests client.store.inventory.get", () => {
  test.concurrent(
    "GET /store/inventory | testId: generated_success | Success test with response schema validation. Expects status code 200",
    async () => {
      const client = new Client({
        apiKey: "API_KEY",
        oauthToken: "API_TOKEN",
        environment: Environment.MockServer,
      });
      // Get both raw response for status and parsed response for data
      const [rawResponse, response] = await Promise.all([
        client.store.inventory.get().asResponse(),
        client.store.inventory.get(),
      ]);
      expect(rawResponse.status).toBe(200); // Exact status code match
      // Response body automatically validated by Zod schema during deserialization
      expect(response).toBeDefined();
    },
  );
});
