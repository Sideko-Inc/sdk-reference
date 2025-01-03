import { types } from "my_petstore_ts";
import {
  ApiPromise,
  CoreClient,
  CoreResourceClient,
  RequestOptions,
} from "my_petstore_ts/core";
import * as requests from "my_petstore_ts/resources/pet/tag/request-types";
import { Schemas$Pet } from "my_petstore_ts/types/pet";
import qs from "qs";
import * as z from "zod";

export class TagClient extends CoreResourceClient {
  constructor(client: CoreClient) {
    super(client);
  }
  /**
   * Multiple tags can be provided with comma separated strings. Use tag1, tag2, tag3 for testing.
   *
   * GET /pet/findByTags
   */
  list(
    request: requests.ListRequest = {},
    opts?: RequestOptions,
  ): ApiPromise<types.Pet[] | types.Pet[]> {
    return this._client.makeRequest({
      method: "get",
      path: "/pet/findByTags",
      auth: ["petstore_auth"],
      query: [qs.stringify({ tags: request.tags }, { arrayFormat: "repeat" })],
      responseType: "json",
      responseSchema: z.union([
        z.array(Schemas$Pet.in),
        z.array(Schemas$Pet.in),
      ]),
      opts,
    });
  }
}
