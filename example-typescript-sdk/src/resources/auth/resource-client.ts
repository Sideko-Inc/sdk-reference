import {
  ApiPromise,
  ApiResponse,
  BinaryResponse,
  CoreClient,
  CoreResourceClient,
  RequestOptions,
  encodeQueryParam,
  zodRequiredAny,
  zodUploadFile,
} from "my_petstore_ts/core";
import * as requests from "my_petstore_ts/resources/auth/request-types";
import * as z from "zod";

export class AuthClient extends CoreResourceClient {
  constructor(client: CoreClient) {
    super(client);
  }
  /**
   * Logs out current logged in user session
   *
   *
   *
   * GET /user/logout
   */
  logout(opts?: RequestOptions): ApiPromise<ApiResponse> {
    return this._client.makeRequest({
      method: "get",
      path: "/user/logout",
      responseRaw: true,
      responseSchema: zodRequiredAny,
      opts,
    });
  }
  /**
   * Logs user into the system
   *
   *
   *
   * GET /user/login
   */
  login(
    request: requests.LoginRequest = {},
    opts?: RequestOptions,
  ): ApiPromise<string | BinaryResponse> {
    return this._client.makeRequest({
      method: "get",
      path: "/user/login",
      query: [
        encodeQueryParam({
          name: "password",
          value: z.string().optional().parse(request.password),
          style: "form",
          explode: true,
        }),
        encodeQueryParam({
          name: "username",
          value: z.string().optional().parse(request.username),
          style: "form",
          explode: true,
        }),
      ],
      responseSchema: z.union([z.string(), zodUploadFile]),
      opts,
    });
  }
}
