import Client, { Environment } from "my_petstore_ts";

describe("tests client.user.delete", () => {
  test.concurrent(
    "DELETE /user/{username} | testId: generated_success | Success test with response schema validation. Expects status code 2xx",
    async () => {
      const client = new Client({
        apiKey: "API_KEY",
        oauthToken: "API_TOKEN",
        environment: Environment.MockServer,
      });
      // Get both raw response for status and parsed response for data
      const [rawResponse, response] = await Promise.all([
        client.user.delete({ username: "string" }).asResponse(),
        client.user.delete({ username: "string" }),
      ]);
      // Verify status code is in 2xx range
      expect(rawResponse.status).toBeGreaterThanOrEqual(200);
      expect(rawResponse.status).toBeLessThan(300);
      // Response body automatically validated by Zod schema during deserialization
      expect(response).toBeDefined();
    },
  );
});

describe("tests client.user.get", () => {
  test.concurrent(
    "GET /user/{username} | testId: generated_success | Success test with response schema validation. Expects status code 200",
    async () => {
      const client = new Client({
        apiKey: "API_KEY",
        oauthToken: "API_TOKEN",
        environment: Environment.MockServer,
      });
      // Get both raw response for status and parsed response for data
      const [rawResponse, response] = await Promise.all([
        client.user.get({ username: "string" }).asResponse(),
        client.user.get({ username: "string" }),
      ]);
      expect(rawResponse.status).toBe(200); // Exact status code match
      // Response body automatically validated by Zod schema during deserialization
      expect(response).toBeDefined();
    },
  );
});

describe("tests client.user.create", () => {
  test.concurrent(
    "POST /user | testId: success_default | Success test with response schema validation. Default response",
    async () => {
      const client = new Client({
        apiKey: "API_KEY",
        oauthToken: "API_TOKEN",
        environment: Environment.MockServer,
      });
      // Verify error response status and rejection
      const rawResponse = await client.user.create().asResponse();
      await expect(client.user.create()).rejects.toThrow();
    },
  );
});

describe("tests client.user.update", () => {
  test.concurrent(
    "PUT /user/{username} | testId: success_default | Empty response test. Default response",
    async () => {
      const client = new Client({
        apiKey: "API_KEY",
        oauthToken: "API_TOKEN",
        environment: Environment.MockServer,
      });
      // Verify error response status and rejection
      const rawResponse = await client.user
        .update({ usernamePath: "string" })
        .asResponse();
      await expect(
        client.user.update({ usernamePath: "string" }),
      ).rejects.toThrow();
    },
  );
});
