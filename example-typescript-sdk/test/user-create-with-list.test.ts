import Client, { Environment } from "my_petstore_ts";

describe("tests client.user.createWithList.create", () => {
  test.concurrent(
    "POST /user/createWithList | testId: success_default | Success test with response schema validation. Expects status code 200",
    async () => {
      const client = new Client({
        apiKey: "API_KEY",
        oauthToken: "API_TOKEN",
        environment: Environment.MockServer,
      });
      // Get both raw response for status and parsed response for data
      const [rawResponse, response] = await Promise.all([
        client.user.createWithList.create({ data: [{}] }).asResponse(),
        client.user.createWithList.create({ data: [{}] }),
      ]);
      expect(rawResponse.status).toBe(200); // Exact status code match
      // Response body automatically validated by Zod schema during deserialization
      expect(response).toBeDefined();
    },
  );
});
