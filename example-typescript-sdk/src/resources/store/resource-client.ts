import { CoreClient, CoreResourceClient } from "my_petstore_ts/core";
import { InventoryClient } from "my_petstore_ts/resources/store/inventory";
import { OrderClient } from "my_petstore_ts/resources/store/order";

export class StoreClient extends CoreResourceClient {
  order: OrderClient;
  inventory: InventoryClient;

  constructor(client: CoreClient) {
    super(client);

    this.order = new OrderClient(this._client);
    this.inventory = new InventoryClient(this._client);
  }
}
