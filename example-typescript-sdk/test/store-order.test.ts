import Client, { Environment } from "my_petstore_ts";

describe("tests client.store.order.delete", () => {
  test.concurrent(
    "DELETE /store/order/{orderId} | testId: generated_success | Success test with response schema validation. Expects status code 2xx",
    async () => {
      const client = new Client({
        apiKey: "API_KEY",
        oauthToken: "API_TOKEN",
        environment: Environment.MockServer,
      });
      // Get both raw response for status and parsed response for data
      const [rawResponse, response] = await Promise.all([
        client.store.order.delete({ orderId: 123 }).asResponse(),
        client.store.order.delete({ orderId: 123 }),
      ]);
      // Verify status code is in 2xx range
      expect(rawResponse.status).toBeGreaterThanOrEqual(200);
      expect(rawResponse.status).toBeLessThan(300);
      // Response body automatically validated by Zod schema during deserialization
      expect(response).toBeDefined();
    },
  );
});

describe("tests client.store.order.get", () => {
  test.concurrent(
    "GET /store/order/{orderId} | testId: generated_success | Success test with response schema validation. Expects status code 200",
    async () => {
      const client = new Client({
        apiKey: "API_KEY",
        oauthToken: "API_TOKEN",
        environment: Environment.MockServer,
      });
      // Get both raw response for status and parsed response for data
      const [rawResponse, response] = await Promise.all([
        client.store.order.get({ orderId: 123 }).asResponse(),
        client.store.order.get({ orderId: 123 }),
      ]);
      expect(rawResponse.status).toBe(200); // Exact status code match
      // Response body automatically validated by Zod schema during deserialization
      expect(response).toBeDefined();
    },
  );
});

describe("tests client.store.order.place", () => {
  test.concurrent(
    "POST /store/order | testId: success_default | Success test with response schema validation. Expects status code 200",
    async () => {
      const client = new Client({
        apiKey: "API_KEY",
        oauthToken: "API_TOKEN",
        environment: Environment.MockServer,
      });
      // Get both raw response for status and parsed response for data
      const [rawResponse, response] = await Promise.all([
        client.store.order.place().asResponse(),
        client.store.order.place(),
      ]);
      expect(rawResponse.status).toBe(200); // Exact status code match
      // Response body automatically validated by Zod schema during deserialization
      expect(response).toBeDefined();
    },
  );
});
