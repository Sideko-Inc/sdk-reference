import { zodTransform } from "my_petstore_ts/core";
import * as z from "zod";

/**
 * ListRequest
 */
export type ListRequest = {
  tags?: string[] | undefined;
};

/**
 * @internal
 * ListRequest without any key transformation, this is what
 * we expect to come in as network data
 */
export type External$ListRequest = {
  tags?: string[] | undefined;
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
    tags: z.array(z.string()).optional(),
  })
  .transform((obj) => {
    return zodTransform(obj, {
      tags: "tags",
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
    tags: z.array(z.string()).optional(),
  })
  .transform((obj) => {
    return zodTransform(obj, {
      tags: "tags",
    });
  });

export const Schemas$ListRequest = {
  in: SchemaIn$ListRequest,
  out: SchemaOut$ListRequest,
};
