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
import * as requests from "my_petstore_ts/resources/store/order/request-types";
import { Schemas$Order } from "my_petstore_ts/types/order";
import * as z from "zod";

export class OrderClient extends CoreResourceClient {
  constructor(client: CoreClient) {
    super(client);
  }
  /**
   * Place an order for a pet
   *
   * Place a new order in the store
   *
   * POST /store/order
   */
  place(
    request: requests.PlaceRequest = {},
    opts?: RequestOptions,
  ): ApiPromise<types.Order> {
    return this._client.makeRequest({
      method: "post",
      path: "/store/order",
      contentType: "application/json",
      body: Schemas$Order.out.parse(request),
      responseSchema: Schemas$Order.in,
      opts,
    });
  }
  /**
   * Find purchase order by ID
   *
   * For valid response try integer IDs with value <= 5 or > 10. Other values will generate exceptions.
   *
   * GET /store/order/{orderId}
   */
  get(
    request: requests.GetRequest,
    opts?: RequestOptions,
  ): ApiPromise<types.Order | BinaryResponse> {
    return this._client.makeRequest({
      method: "get",
      path: `/store/order/${request.orderId}`,
      responseSchema: z.union([Schemas$Order.in, zodUploadFile]),
      opts,
    });
  }
  /**
   * Delete purchase order by ID
   *
   * For valid response try integer IDs with value < 1000. Anything above 1000 or nonintegers will generate API errors
   *
   * DELETE /store/order/{orderId}
   */
  delete(
    request: requests.DeleteRequest,
    opts?: RequestOptions,
  ): ApiPromise<ApiResponse> {
    return this._client.makeRequest({
      method: "delete",
      path: `/store/order/${request.orderId}`,
      responseRaw: true,
      responseSchema: zodRequiredAny,
      opts,
    });
  }
}
