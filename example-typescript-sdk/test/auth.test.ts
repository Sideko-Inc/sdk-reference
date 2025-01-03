import Client, { Environment } from "my_petstore_ts";

describe("tests client.auth.login", () => {
  test.concurrent(
    "GET /user/login | testId: generated_success | Success test with response schema validation. Expects status code 200",
    async () => {
      const client = new Client({
        apiKey: "API_KEY",
        oauthToken: "API_TOKEN",
        environment: Environment.MockServer,
      });
      // Get both raw response for status and parsed response for data
      const [rawResponse, response] = await Promise.all([
        client.auth.login().asResponse(),
        client.auth.login(),
      ]);
      expect(rawResponse.status).toBe(200); // Exact status code match
      // Response body automatically validated by Zod schema during deserialization
      expect(response).toBeDefined();
    },
  );
});

describe("tests client.auth.logout", () => {
  test.concurrent(
    "GET /user/logout | testId: generated_success | Empty response test. Default response",
    async () => {
      const client = new Client({
        apiKey: "API_KEY",
        oauthToken: "API_TOKEN",
        environment: Environment.MockServer,
      });
      // Verify error response status and rejection
      const rawResponse = await client.auth.logout().asResponse();
      await expect(client.auth.logout()).rejects.toThrow();
    },
  );
});
