import {
  ApiPromise,
  CoreClient,
  CoreResourceClient,
  RequestOptions,
} from "my_petstore_ts/core";
import * as requests from "my_petstore_ts/resources/auth/request-types";
import qs from "qs";
import * as z from "zod";

export class AuthClient extends CoreResourceClient {
  constructor(client: CoreClient) {
    super(client);
  }
  /**
   *
   *
   * GET /user/logout
   */
  logout(opts?: RequestOptions): ApiPromise<null> {
    return this._client.makeRequest({
      method: "get",
      path: "/user/logout",
      responseType: "json",
      opts,
    });
  }
  /**
   *
   *
   * GET /user/login
   */
  login(
    request: requests.LoginRequest = {},
    opts?: RequestOptions,
  ): ApiPromise<string | string> {
    return this._client.makeRequest({
      method: "get",
      path: "/user/login",
      query: [
        qs.stringify({ password: request.password }),
        qs.stringify({ username: request.username }),
      ],
      responseType: "json",
      responseSchema: z.union([z.string(), z.string()]),
      opts,
    });
  }
}
