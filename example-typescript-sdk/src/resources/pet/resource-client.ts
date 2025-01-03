import { types } from "my_petstore_ts";
import {
  ApiPromise,
  BinaryResponse,
  CoreClient,
  CoreResourceClient,
  RequestOptions,
  zodUploadFile,
} from "my_petstore_ts/core";
import { ImageClient } from "my_petstore_ts/resources/pet/image";
import * as requests from "my_petstore_ts/resources/pet/request-types";
import { StatusClient } from "my_petstore_ts/resources/pet/status";
import { TagClient } from "my_petstore_ts/resources/pet/tag";
import { Schemas$Pet } from "my_petstore_ts/types/pet";
import qs from "qs";
import * as z from "zod";

export class PetClient extends CoreResourceClient {
  status: StatusClient;
  tag: TagClient;
  image: ImageClient;

  constructor(client: CoreClient) {
    super(client);

    this.status = new StatusClient(this._client);
    this.tag = new TagClient(this._client);
    this.image = new ImageClient(this._client);
  }
  /**
   * Update an existing pet by Id
   *
   * PUT /pet
   */
  update(
    request: requests.UpdateRequest,
    opts?: RequestOptions,
  ): ApiPromise<types.Pet | types.Pet> {
    return this._client.makeRequest({
      method: "put",
      path: "/pet",
      auth: ["petstore_auth"],
      contentType: "application/json",
      body: Schemas$Pet.out.parse(request),
      responseType: "json",
      responseSchema: z.union([Schemas$Pet.in, Schemas$Pet.in]),
      opts,
    });
  }
  /**
   *
   *
   * POST /pet/{petId}
   */
  updateForm(
    request: requests.UpdateFormRequest,
    opts?: RequestOptions,
  ): ApiPromise<BinaryResponse> {
    return this._client.makeRequest({
      method: "post",
      path: `/pet/${request.petId}`,
      auth: ["petstore_auth"],
      query: [
        qs.stringify({ name: request.name }),
        qs.stringify({ status: request.status }),
      ],
      responseType: "blob",
      responseSchema: zodUploadFile,
      opts,
    });
  }
  /**
   * Add a new pet to the store
   *
   * POST /pet
   */
  create(
    request: requests.CreateRequest,
    opts?: RequestOptions,
  ): ApiPromise<types.Pet | types.Pet> {
    return this._client.makeRequest({
      method: "post",
      path: "/pet",
      auth: ["petstore_auth"],
      contentType: "application/json",
      body: Schemas$Pet.out.parse(request),
      responseType: "json",
      responseSchema: z.union([Schemas$Pet.in, Schemas$Pet.in]),
      opts,
    });
  }
  /**
   * Returns a single pet
   *
   * GET /pet/{petId}
   */
  get(
    request: requests.GetRequest,
    opts?: RequestOptions,
  ): ApiPromise<types.Pet | types.Pet> {
    return this._client.makeRequest({
      method: "get",
      path: `/pet/${request.petId}`,
      auth: ["api_key", "petstore_auth"],
      responseType: "json",
      responseSchema: z.union([Schemas$Pet.in, Schemas$Pet.in]),
      opts,
    });
  }
  /**
   *
   *
   * DELETE /pet/{petId}
   */
  delete(
    request: requests.DeleteRequest,
    opts?: RequestOptions,
  ): ApiPromise<BinaryResponse> {
    return this._client.makeRequest({
      method: "delete",
      path: `/pet/${request.petId}`,
      auth: ["petstore_auth"],
      responseType: "blob",
      responseSchema: zodUploadFile,
      opts,
    });
  }
}
