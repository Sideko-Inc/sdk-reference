import Client, { Environment } from "my_petstore_ts";

describe("tests client.pet.delete", () => {
  test.concurrent(
    "DELETE /pet/{petId} | testId: generated_success | Success test with response schema validation. Expects status code 2xx",
    async () => {
      const client = new Client({
        apiKey: "API_KEY",
        oauthToken: "API_TOKEN",
        environment: Environment.MockServer,
      });
      // Get both raw response for status and parsed response for data
      const [rawResponse, response] = await Promise.all([
        client.pet.delete({ petId: 123 }).asResponse(),
        client.pet.delete({ petId: 123 }),
      ]);
      // Verify status code is in 2xx range
      expect(rawResponse.status).toBeGreaterThanOrEqual(200);
      expect(rawResponse.status).toBeLessThan(300);
      // Response body automatically validated by Zod schema during deserialization
      expect(response).toBeDefined();
    },
  );
});

describe("tests client.pet.get", () => {
  test.concurrent(
    "GET /pet/{petId} | testId: generated_success | Success test with response schema validation. Expects status code 200",
    async () => {
      const client = new Client({
        apiKey: "API_KEY",
        oauthToken: "API_TOKEN",
        environment: Environment.MockServer,
      });
      // Get both raw response for status and parsed response for data
      const [rawResponse, response] = await Promise.all([
        client.pet.get({ petId: 123 }).asResponse(),
        client.pet.get({ petId: 123 }),
      ]);
      expect(rawResponse.status).toBe(200); // Exact status code match
      // Response body automatically validated by Zod schema during deserialization
      expect(response).toBeDefined();
    },
  );
});

describe("tests client.pet.create", () => {
  test.concurrent(
    "POST /pet | testId: success_default | Success test with response schema validation. Expects status code 200",
    async () => {
      const client = new Client({
        apiKey: "API_KEY",
        oauthToken: "API_TOKEN",
        environment: Environment.MockServer,
      });
      // Get both raw response for status and parsed response for data
      const [rawResponse, response] = await Promise.all([
        client.pet
          .create({ name: "doggie", photoUrls: ["string"] })
          .asResponse(),
        client.pet.create({ name: "doggie", photoUrls: ["string"] }),
      ]);
      expect(rawResponse.status).toBe(200); // Exact status code match
      // Response body automatically validated by Zod schema during deserialization
      expect(response).toBeDefined();
    },
  );
});

describe("tests client.pet.updateForm", () => {
  test.concurrent(
    "POST /pet/{petId} | testId: generated_success | Success test with response schema validation. Expects status code 2xx",
    async () => {
      const client = new Client({
        apiKey: "API_KEY",
        oauthToken: "API_TOKEN",
        environment: Environment.MockServer,
      });
      // Get both raw response for status and parsed response for data
      const [rawResponse, response] = await Promise.all([
        client.pet.updateForm({ petId: 123 }).asResponse(),
        client.pet.updateForm({ petId: 123 }),
      ]);
      // Verify status code is in 2xx range
      expect(rawResponse.status).toBeGreaterThanOrEqual(200);
      expect(rawResponse.status).toBeLessThan(300);
      // Response body automatically validated by Zod schema during deserialization
      expect(response).toBeDefined();
    },
  );
});

describe("tests client.pet.update", () => {
  test.concurrent(
    "PUT /pet | testId: success_default | Success test with response schema validation. Expects status code 200",
    async () => {
      const client = new Client({
        apiKey: "API_KEY",
        oauthToken: "API_TOKEN",
        environment: Environment.MockServer,
      });
      // Get both raw response for status and parsed response for data
      const [rawResponse, response] = await Promise.all([
        client.pet
          .update({ name: "doggie", photoUrls: ["string"] })
          .asResponse(),
        client.pet.update({ name: "doggie", photoUrls: ["string"] }),
      ]);
      expect(rawResponse.status).toBe(200); // Exact status code match
      // Response body automatically validated by Zod schema during deserialization
      expect(response).toBeDefined();
    },
  );
});
