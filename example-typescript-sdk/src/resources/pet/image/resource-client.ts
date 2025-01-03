import { types } from "my_petstore_ts";
import {
  ApiPromise,
  CoreClient,
  CoreResourceClient,
  RequestOptions,
  zodUploadFile,
} from "my_petstore_ts/core";
import * as requests from "my_petstore_ts/resources/pet/image/request-types";
import { Schemas$ApiResponse } from "my_petstore_ts/types/api-response";
import qs from "qs";

export class ImageClient extends CoreResourceClient {
  constructor(client: CoreClient) {
    super(client);
  }
  /**
   *
   *
   * POST /pet/{petId}/uploadImage
   */
  upload(
    request: requests.UploadRequest,
    opts?: RequestOptions,
  ): ApiPromise<types.ApiResponse> {
    return this._client.makeRequest({
      method: "post",
      path: `/pet/${request.petId}/uploadImage`,
      auth: ["petstore_auth"],
      query: [qs.stringify({ additionalMetadata: request.additionalMetadata })],
      contentType: "application/octet-stream",
      body: zodUploadFile.parse(request.data),
      responseType: "json",
      responseSchema: Schemas$ApiResponse.in,
      opts,
    });
  }
}
