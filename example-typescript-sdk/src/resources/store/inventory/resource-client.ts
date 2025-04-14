import { types } from "my_petstore_ts";
import {
  ApiPromise,
  CoreClient,
  CoreResourceClient,
  RequestOptions,
} from "my_petstore_ts/core";
import { Schemas$StoreInventoryGetResponse } from "my_petstore_ts/types/store-inventory-get-response";

export class InventoryClient extends CoreResourceClient {
  constructor(client: CoreClient) {
    super(client);
  }
  /**
   * Returns pet inventories by status
   *
   * Returns a map of status codes to quantities
   *
   * GET /store/inventory
   */
  get(opts?: RequestOptions): ApiPromise<types.StoreInventoryGetResponse> {
    return this._client.makeRequest({
      method: "get",
      path: "/store/inventory",
      auth: ["api_key"],
      responseSchema: Schemas$StoreInventoryGetResponse.in,
      opts,
    });
  }
}
