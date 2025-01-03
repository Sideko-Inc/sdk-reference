import { types } from "my_petstore_ts";
import {
  ApiPromise,
  CoreClient,
  CoreResourceClient,
  RequestOptions,
} from "my_petstore_ts/core";
import * as requests from "my_petstore_ts/resources/pet/status/request-types";
import { Schemas$Pet } from "my_petstore_ts/types/pet";
import qs from "qs";
import * as z from "zod";

export class StatusClient extends CoreResourceClient {
  constructor(client: CoreClient) {
    super(client);
  }
  /**
   * Multiple status values can be provided with comma separated strings
   *
   * GET /pet/findByStatus
   */
  list(
    request: requests.ListRequest = {},
    opts?: RequestOptions,
  ): ApiPromise<types.Pet[] | types.Pet[]> {
    return this._client.makeRequest({
      method: "get",
      path: "/pet/findByStatus",
      auth: ["petstore_auth"],
      query: [qs.stringify({ status: request.status })],
      responseType: "json",
      responseSchema: z.union([
        z.array(Schemas$Pet.in),
        z.array(Schemas$Pet.in),
      ]),
      opts,
    });
  }
}
