import { types } from "my_petstore_ts";
import {
  ApiPromise,
  ApiResponse,
  BinaryResponse,
  CoreClient,
  CoreResourceClient,
  RequestOptions,
  zodRequiredAny,
  zodUploadFile,
} from "my_petstore_ts/core";
import { CreateWithListClient } from "my_petstore_ts/resources/user/create-with-list";
import * as requests from "my_petstore_ts/resources/user/request-types";
import { Schemas$User } from "my_petstore_ts/types/user";
import * as z from "zod";

export class UserClient extends CoreResourceClient {
  createWithList: CreateWithListClient;

  constructor(client: CoreClient) {
    super(client);

    this.createWithList = new CreateWithListClient(this._client);
  }
  /**
   * Update user
   *
   * This can only be done by the logged in user.
   *
   * PUT /user/{username}
   */
  update(
    request: requests.UpdateRequest,
    opts?: RequestOptions,
  ): ApiPromise<ApiResponse> {
    return this._client.makeRequest({
      method: "put",
      path: `/user/${request.usernamePath}`,
      contentType: "application/json",
      body: Schemas$User.out.parse(request),
      responseRaw: true,
      responseSchema: zodRequiredAny,
      opts,
    });
  }
  /**
   * Create user
   *
   * This can only be done by the logged in user.
   *
   * POST /user
   */
  create(
    request: requests.CreateRequest = {},
    opts?: RequestOptions,
  ): ApiPromise<types.User | BinaryResponse> {
    return this._client.makeRequest({
      method: "post",
      path: "/user",
      contentType: "application/json",
      body: Schemas$User.out.parse(request),
      responseSchema: z.union([Schemas$User.in, zodUploadFile]),
      opts,
    });
  }
  /**
   * Get user by user name
   *
   *
   *
   * GET /user/{username}
   */
  get(
    request: requests.GetRequest,
    opts?: RequestOptions,
  ): ApiPromise<types.User | BinaryResponse> {
    return this._client.makeRequest({
      method: "get",
      path: `/user/${request.username}`,
      responseSchema: z.union([Schemas$User.in, zodUploadFile]),
      opts,
    });
  }
  /**
   * Delete user
   *
   * This can only be done by the logged in user.
   *
   * DELETE /user/{username}
   */
  delete(
    request: requests.DeleteRequest,
    opts?: RequestOptions,
  ): ApiPromise<ApiResponse> {
    return this._client.makeRequest({
      method: "delete",
      path: `/user/${request.username}`,
      responseRaw: true,
      responseSchema: zodRequiredAny,
      opts,
    });
  }
}
