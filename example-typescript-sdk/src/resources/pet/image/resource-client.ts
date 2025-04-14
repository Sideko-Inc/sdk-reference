import { types } from "my_petstore_ts";
import {
  ApiPromise,
  CoreClient,
  CoreResourceClient,
  RequestOptions,
  encodeQueryParam,
  zodUploadFile,
} from "my_petstore_ts/core";
import * as requests from "my_petstore_ts/resources/pet/image/request-types";
import { Schemas$ApiRes } from "my_petstore_ts/types/api-response";
import * as z from "zod";

export class ImageClient extends CoreResourceClient {
  constructor(client: CoreClient) {
    super(client);
  }
  /**
   * uploads an image
   *
   *
   *
   * POST /pet/{petId}/uploadImage
   */
  upload(
    request: requests.UploadRequest,
    opts?: RequestOptions,
  ): ApiPromise<types.ApiRes> {
    return this._client.makeRequest({
      method: "post",
      path: `/pet/${request.petId}/uploadImage`,
      auth: ["petstore_auth"],
      query: [
        encodeQueryParam({
          name: "additionalMetadata",
          value: z.string().optional().parse(request.additionalMetadata),
          style: "form",
          explode: true,
        }),
      ],
      contentType: "application/octet-stream",
      body: zodUploadFile.parse(request.data),
      responseSchema: Schemas$ApiRes.in,
      opts,
    });
  }
}
