import { AuthBearer, AuthKeyHeader, CoreClient } from "my_petstore_ts/core";
import { Environment } from "my_petstore_ts/environment";
import { AuthClient } from "my_petstore_ts/resources/auth";
import { PetClient } from "my_petstore_ts/resources/pet";
import { StoreClient } from "my_petstore_ts/resources/store";
import { UserClient } from "my_petstore_ts/resources/user";

export interface ClientOptions {
  baseUrl?: string;
  environment?: Environment;
  timeout?: number;
  apiKey?: string;
  oauthToken?: string;
}

export class Client {
  protected _client: CoreClient;
  pet: PetClient;
  store: StoreClient;
  user: UserClient;
  auth: AuthClient;

  constructor(opts?: ClientOptions) {
    const baseUrl =
      opts?.baseUrl ?? opts?.environment ?? Environment.Environment;
    this._client = new CoreClient({ baseUrl, timeout: opts?.timeout });
    this._client.registerAuth(
      "api_key",
      new AuthKeyHeader("api_key", opts?.apiKey),
    );
    this._client.registerAuth(
      "petstore_auth",
      new AuthBearer(opts?.oauthToken),
    );

    this.pet = new PetClient(this._client);
    this.store = new StoreClient(this._client);
    this.user = new UserClient(this._client);
    this.auth = new AuthClient(this._client);
  }
}
