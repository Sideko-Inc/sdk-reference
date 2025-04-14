import { types } from "my_petstore_ts";
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
import { ImageClient } from "my_petstore_ts/resources/pet/image";
import * as requests from "my_petstore_ts/resources/pet/request-types";
import { StatusClient } from "my_petstore_ts/resources/pet/status";
import { TagClient } from "my_petstore_ts/resources/pet/tag";
import { Schemas$Pet } from "my_petstore_ts/types/pet";
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
   * Update an existing pet
   *
   * Update an existing pet by Id
   *
   * PUT /pet
   */
  update(
    request: requests.UpdateRequest,
    opts?: RequestOptions,
  ): ApiPromise<types.Pet | BinaryResponse> {
    return this._client.makeRequest({
      method: "put",
      path: "/pet",
      auth: ["petstore_auth"],
      contentType: "application/json",
      body: Schemas$Pet.out.parse(request),
      responseSchema: z.union([Schemas$Pet.in, zodUploadFile]),
      opts,
    });
  }
  /**
   * Updates a pet in the store with form data
   *
   *
   *
   * POST /pet/{petId}
   */
  updateForm(
    request: requests.UpdateFormRequest,
    opts?: RequestOptions,
  ): ApiPromise<ApiResponse> {
    return this._client.makeRequest({
      method: "post",
      path: `/pet/${request.petId}`,
      auth: ["petstore_auth"],
      query: [
        encodeQueryParam({
          name: "name",
          value: z.string().optional().parse(request.name),
          style: "form",
          explode: true,
        }),
        encodeQueryParam({
          name: "status",
          value: z.string().optional().parse(request.status),
          style: "form",
          explode: true,
        }),
      ],
      responseRaw: true,
      responseSchema: zodRequiredAny,
      opts,
    });
  }
  /**
   * Add a new pet to the store
   *
   * Add a new pet to the store
   *
   * POST /pet
   */
  create(
    request: requests.CreateRequest,
    opts?: RequestOptions,
  ): ApiPromise<types.Pet | BinaryResponse> {
    return this._client.makeRequest({
      method: "post",
      path: "/pet",
      auth: ["petstore_auth"],
      contentType: "application/json",
      body: Schemas$Pet.out.parse(request),
      responseSchema: z.union([Schemas$Pet.in, zodUploadFile]),
      opts,
    });
  }
  /**
   * Find pet by ID
   *
   * Returns a single pet
   *
   * GET /pet/{petId}
   */
  get(
    request: requests.GetRequest,
    opts?: RequestOptions,
  ): ApiPromise<types.Pet | BinaryResponse> {
    return this._client.makeRequest({
      method: "get",
      path: `/pet/${request.petId}`,
      auth: ["api_key", "petstore_auth"],
      responseSchema: z.union([Schemas$Pet.in, zodUploadFile]),
      opts,
    });
  }
  /**
   * Deletes a pet
   *
   *
   *
   * DELETE /pet/{petId}
   */
  delete(
    request: requests.DeleteRequest,
    opts?: RequestOptions,
  ): ApiPromise<ApiResponse> {
    return this._client.makeRequest({
      method: "delete",
      path: `/pet/${request.petId}`,
      auth: ["petstore_auth"],
      responseRaw: true,
      responseSchema: zodRequiredAny,
      opts,
    });
  }
}
