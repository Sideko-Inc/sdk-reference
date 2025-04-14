import { types } from "my_petstore_ts";
import {
  ApiPromise,
  BinaryResponse,
  CoreClient,
  CoreResourceClient,
  RequestOptions,
  zodUploadFile,
} from "my_petstore_ts/core";
import * as requests from "my_petstore_ts/resources/user/create-with-list/request-types";
import { Schemas$User } from "my_petstore_ts/types/user";
import * as z from "zod";

export class CreateWithListClient extends CoreResourceClient {
  constructor(client: CoreClient) {
    super(client);
  }
  /**
   * Creates list of users with given input array
   *
   * Creates list of users with given input array
   *
   * POST /user/createWithList
   */
  create(
    request: requests.CreateRequest,
    opts?: RequestOptions,
  ): ApiPromise<types.User | BinaryResponse> {
    return this._client.makeRequest({
      method: "post",
      path: "/user/createWithList",
      contentType: "application/json",
      body: z.array(Schemas$User.out).parse(request.data),
      responseSchema: z.union([Schemas$User.in, zodUploadFile]),
      opts,
    });
  }
}
