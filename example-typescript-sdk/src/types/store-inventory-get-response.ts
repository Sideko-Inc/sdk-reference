import { zodTransform } from "my_petstore_ts/core";
import * as z from "zod";

/**
 * StoreInventoryGetResponse
 */
export type StoreInventoryGetResponse = {
  [additionalProperty: string]: number | null | undefined;
};

/**
 * @internal
 * StoreInventoryGetResponse without any key transformation, this is what
 * we expect to come in as network data
 */
export type External$StoreInventoryGetResponse = {
  [additionalProperty: string]:
    | External$StoreInventoryGetResponse
    | null
    | undefined;
};

/**
 * Takes network data, validates it, and transforms keys to match typescript object StoreInventoryGetResponse
 */
const SchemaIn$StoreInventoryGetResponse: z.ZodType<
  StoreInventoryGetResponse, // output type of this zod object
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
 * Takes typescript data, validates it, and maps keys to match the expected external object External$StoreInventoryGetResponse
 */
const SchemaOut$StoreInventoryGetResponse: z.ZodType<
  External$StoreInventoryGetResponse, // output type of this zod object
  z.ZodTypeDef,
  StoreInventoryGetResponse // the object to be transformed
> = z
  .object({})
  .catchall(z.number().int())
  .transform((obj) => {
    return zodTransform(obj, {});
  });

export const Schemas$StoreInventoryGetResponse = {
  in: SchemaIn$StoreInventoryGetResponse,
  out: SchemaOut$StoreInventoryGetResponse,
};
