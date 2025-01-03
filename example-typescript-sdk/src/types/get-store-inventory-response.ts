import { zodTransform } from "my_petstore_ts/core";
import * as z from "zod";

/**
 * GetStoreInventoryResponse
 */
export type GetStoreInventoryResponse = {
  [additionalProperty: string]: number | null | undefined;
};

/**
 * @internal
 * GetStoreInventoryResponse without any key transformation, this is what
 * we expect to come in as network data
 */
export type External$GetStoreInventoryResponse = {
  [additionalProperty: string]:
    | External$GetStoreInventoryResponse
    | null
    | undefined;
};

/**
 * Takes network data, validates it, and transforms keys to match typescript object GetStoreInventoryResponse
 */
const SchemaIn$GetStoreInventoryResponse: z.ZodType<
  GetStoreInventoryResponse, // output type of this zod object
  z.ZodTypeDef,
  unknown
> = z
  .object({})
  .catchall(z.number().int())
  .transform((obj) => {
    return zodTransform(obj, {});
  });

/**
 * @internal
 * Takes typescript data, validates it, and maps keys to match the expected external object External$GetStoreInventoryResponse
 */
const SchemaOut$GetStoreInventoryResponse: z.ZodType<
  External$GetStoreInventoryResponse, // output type of this zod object
  z.ZodTypeDef,
  GetStoreInventoryResponse // the object to be transformed
> = z
  .object({})
  .catchall(z.number().int())
  .transform((obj) => {
    return zodTransform(obj, {});
  });

export const Schemas$GetStoreInventoryResponse = {
  in: SchemaIn$GetStoreInventoryResponse,
  out: SchemaOut$GetStoreInventoryResponse,
};
