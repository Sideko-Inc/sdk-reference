import { zodTransform } from "my_petstore_ts/core";
import {
  External$GetPetFindByStatusStatusEnum,
  GetPetFindByStatusStatusEnum,
} from "my_petstore_ts/types/get-pet-find-by-status-status-enum";
import * as z from "zod";

/**
 * ListRequest
 */
export type ListRequest = {
  status?: GetPetFindByStatusStatusEnum | undefined;
};

/**
 * @internal
 * ListRequest without any key transformation, this is what
 * we expect to come in as network data
 */
export type External$ListRequest = {
  status?: External$GetPetFindByStatusStatusEnum | undefined;
};

/**
 * Takes network data, validates it, and transforms keys to match typescript object ListRequest
 */
const SchemaIn$ListRequest: z.ZodType<
  ListRequest, // output type of this zod object
  z.ZodTypeDef,
  unknown
> = z
  .object({
    status: z.enum(["available", "pending", "sold"]).optional(),
  })
  .transform((obj) => {
    return zodTransform(obj, {
      status: "status",
    });
  });

/**
 * @internal
 * Takes typescript data, validates it, and maps keys to match the expected external object External$ListRequest
 */
const SchemaOut$ListRequest: z.ZodType<
  External$ListRequest, // output type of this zod object
  z.ZodTypeDef,
  ListRequest // the object to be transformed
> = z
  .object({
    status: z.enum(["available", "pending", "sold"]).optional(),
  })
  .transform((obj) => {
    return zodTransform(obj, {
      status: "status",
    });
  });

export const Schemas$ListRequest = {
  in: SchemaIn$ListRequest,
  out: SchemaOut$ListRequest,
};
