import { zodTransform } from "my_petstore_ts/core";
import * as z from "zod";

/**
 * User
 */
export type User = {
  email?: string | undefined;
  firstName?: string | undefined;
  id?: number | undefined;
  lastName?: string | undefined;
  password?: string | undefined;
  phone?: string | undefined;
  /**
   * User Status
   */
  userStatus?: number | undefined;
  username?: string | undefined;
};

/**
 * @internal
 * User without any key transformation, this is what
 * we expect to come in as network data
 */
export type External$User = {
  email?: string | undefined;
  firstName?: string | undefined;
  id?: number | undefined;
  lastName?: string | undefined;
  password?: string | undefined;
  phone?: string | undefined;
  userStatus?: number | undefined;
  username?: string | undefined;
};

/**
 * Takes network data, validates it, and transforms keys to match typescript object User
 */
const SchemaIn$User: z.ZodType<
  User, // output type of this zod object
  z.ZodTypeDef,
  unknown
> = z
  .object({
    email: z.string().optional(),
    firstName: z.string().optional(),
    id: z.number().int().optional(),
    lastName: z.string().optional(),
    password: z.string().optional(),
    phone: z.string().optional(),
    userStatus: z.number().int().optional(),
    username: z.string().optional(),
  })
  .transform((obj) => {
    return zodTransform(obj, {
      email: "email",
      firstName: "firstName",
      id: "id",
      lastName: "lastName",
      password: "password",
      phone: "phone",
      userStatus: "userStatus",
      username: "username",
    });
  });

/**
 * @internal
 * Takes typescript data, validates it, and maps keys to match the expected external object External$User
 */
const SchemaOut$User: z.ZodType<
  External$User, // output type of this zod object
  z.ZodTypeDef,
  User // the object to be transformed
> = z
  .object({
    email: z.string().optional(),
    firstName: z.string().optional(),
    id: z.number().int().optional(),
    lastName: z.string().optional(),
    password: z.string().optional(),
    phone: z.string().optional(),
    userStatus: z.number().int().optional(),
    username: z.string().optional(),
  })
  .transform((obj) => {
    return zodTransform(obj, {
      email: "email",
      firstName: "firstName",
      id: "id",
      lastName: "lastName",
      password: "password",
      phone: "phone",
      userStatus: "userStatus",
      username: "username",
    });
  });

export const Schemas$User = {
  in: SchemaIn$User,
  out: SchemaOut$User,
};
