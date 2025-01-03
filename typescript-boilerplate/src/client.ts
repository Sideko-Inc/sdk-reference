export interface SidekoClientOptions {
  baseUrl?: string;
  environment?: Environment;
  timeout?: number;
}

export class SidekoClient {
  protected _client: CoreClient;

  constructor(opts?: SidekoClientOptions) {
    
  }
}
