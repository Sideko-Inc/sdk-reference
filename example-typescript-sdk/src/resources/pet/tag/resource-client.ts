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
import * as requests from "my_petstore_ts/resources/pet/tag/request-types";
import { Schemas$Pet } from "my_petstore_ts/types/pet";
import * as z from "zod";

export class TagClient extends CoreResourceClient {
  constructor(client: CoreClient) {
    super(client);
  }
  /**
   * Finds Pets by tags
   *
   * Multiple tags can be provided with comma separated strings. Use tag1, tag2, tag3 for testing.
   *
   * GET /pet/findByTags
   */
  list(
    request: requests.ListRequest = {},
    opts?: RequestOptions,
  ): ApiPromise<types.Pet[] | BinaryResponse> {
    return this._client.makeRequest({
      method: "get",
      path: "/pet/findByTags",
      auth: ["petstore_auth"],
      query: [
        encodeQueryParam({
          name: "tags",
          value: z.array(z.string()).optional().parse(request.tags),
          style: "form",
          explode: true,
        }),
      ],
      responseSchema: z.union([z.array(Schemas$Pet.in), zodUploadFile]),
      opts,
    });
  }
}
