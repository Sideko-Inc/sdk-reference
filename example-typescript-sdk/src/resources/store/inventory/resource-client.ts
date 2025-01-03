import { types } from "my_petstore_ts";
import {
  ApiPromise,
  CoreClient,
  CoreResourceClient,
  RequestOptions,
} from "my_petstore_ts/core";
import { Schemas$GetStoreInventoryResponse } from "my_petstore_ts/types/get-store-inventory-response";

export class InventoryClient extends CoreResourceClient {
  constructor(client: CoreClient) {
    super(client);
  }
  /**
   * Returns a map of status codes to quantities
   *
   * GET /store/inventory
   */
  get(opts?: RequestOptions): ApiPromise<types.GetStoreInventoryResponse> {
    return this._client.makeRequest({
      method: "get",
      path: "/store/inventory",
      auth: ["api_key"],
      responseType: "json",
      responseSchema: Schemas$GetStoreInventoryResponse.in,
      opts,
    });
  }
}
