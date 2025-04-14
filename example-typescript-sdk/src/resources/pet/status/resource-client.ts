import { types } from "my_petstore_ts";
import {
  ApiPromise,
  BinaryResponse,
  CoreClient,
  CoreResourceClient,
  RequestOptions,
  encodeQueryParam,
  zodUploadFile,
} from "my_petstore_ts/core";
import * as requests from "my_petstore_ts/resources/pet/status/request-types";
import { Schemas$Pet } from "my_petstore_ts/types/pet";
import * as z from "zod";

export class StatusClient extends CoreResourceClient {
  constructor(client: CoreClient) {
    super(client);
  }
  /**
   * Finds Pets by status
   *
   * Multiple status values can be provided with comma separated strings
   *
   * GET /pet/findByStatus
   */
  list(
    request: requests.ListRequest = {},
    opts?: RequestOptions,
  ): ApiPromise<types.Pet[] | BinaryResponse> {
    return this._client.makeRequest({
      method: "get",
      path: "/pet/findByStatus",
      auth: ["petstore_auth"],
      query: [
        encodeQueryParam({
          name: "status",
          value: z
            .enum(["available", "pending", "sold"])
            .optional()
            .parse(request.status),
          style: "form",
          explode: true,
        }),
      ],
      responseSchema: z.union([z.array(Schemas$Pet.in), zodUploadFile]),
      opts,
    });
  }
}
