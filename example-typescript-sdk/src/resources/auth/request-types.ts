import { zodTransform } from "my_petstore_ts/core";
import * as z from "zod";

/**
 * LoginRequest
 */
export type LoginRequest = {
  password?: string | undefined;
  username?: string | undefined;
};

/**
 * @internal
 * LoginRequest without any key transformation, this is what
 * we expect to come in as network data
 */
export type External$LoginRequest = {
  password?: string | undefined;
  username?: string | undefined;
};

/**
 * Takes network data, validates it, and transforms keys to match typescript object LoginRequest
 */
const SchemaIn$LoginRequest: z.ZodType<
  LoginRequest, // output type of this zod object
  z.ZodTypeDef,
  unknown
> = z
  .object({
    password: z.string().optional(),
    username: z.string().optional(),
  })
  .transform((obj) => {
    return zodTransform(obj, {
      password: "password",
      username: "username",
    });
  });

/**
 * @internal
 * Takes typescript data, validates it, and maps keys to match the expected external object External$LoginRequest
 */
const SchemaOut$LoginRequest: z.ZodType<
  External$LoginRequest, // output type of this zod object
  z.ZodTypeDef,
  LoginRequest // the object to be transformed
> = z
  .object({
    password: z.string().optional(),
    username: z.string().optional(),
  })
  .transform((obj) => {
    return zodTransform(obj, {
      password: "password",
      username: "username",
    });
  });

export const Schemas$LoginRequest = {
  in: SchemaIn$LoginRequest,
  out: SchemaOut$LoginRequest,
};
