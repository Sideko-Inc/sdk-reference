import { zodTransform } from "my_petstore_ts/core";
import * as z from "zod";

/**
 * DeleteRequest
 */
export type DeleteRequest = {
  username: string;
};

/**
 * @internal
 * DeleteRequest without any key transformation, this is what
 * we expect to come in as network data
 */
export type External$DeleteRequest = {
  username: string;
};

/**
 * Takes network data, validates it, and transforms keys to match typescript object DeleteRequest
 */
const SchemaIn$DeleteRequest: z.ZodType<
  DeleteRequest, // output type of this zod object
  z.ZodTypeDef,
  unknown
> = z
  .object({
    username: z.string(),
  })
  .transform((obj) => {
    return zodTransform(obj, {
      username: "username",
    });
  });

/**
 * @internal
 * Takes typescript data, validates it, and maps keys to match the expected external object External$DeleteRequest
 */
const SchemaOut$DeleteRequest: z.ZodType<
  External$DeleteRequest, // output type of this zod object
  z.ZodTypeDef,
  DeleteRequest // the object to be transformed
> = z
  .object({
    username: z.string(),
  })
  .transform((obj) => {
    return zodTransform(obj, {
      username: "username",
    });
  });

export const Schemas$DeleteRequest = {
  in: SchemaIn$DeleteRequest,
  out: SchemaOut$DeleteRequest,
};

/**
 * GetRequest
 */
export type GetRequest = {
  username: string;
};

/**
 * @internal
 * GetRequest without any key transformation, this is what
 * we expect to come in as network data
 */
export type External$GetRequest = {
  username: string;
};

/**
 * Takes network data, validates it, and transforms keys to match typescript object GetRequest
 */
const SchemaIn$GetRequest: z.ZodType<
  GetRequest, // output type of this zod object
  z.ZodTypeDef,
  unknown
> = z
  .object({
    username: z.string(),
  })
  .transform((obj) => {
    return zodTransform(obj, {
      username: "username",
    });
  });

/**
 * @internal
 * Takes typescript data, validates it, and maps keys to match the expected external object External$GetRequest
 */
const SchemaOut$GetRequest: z.ZodType<
  External$GetRequest, // output type of this zod object
  z.ZodTypeDef,
  GetRequest // the object to be transformed
> = z
  .object({
    username: z.string(),
  })
  .transform((obj) => {
    return zodTransform(obj, {
      username: "username",
    });
  });

export const Schemas$GetRequest = {
  in: SchemaIn$GetRequest,
  out: SchemaOut$GetRequest,
};

/**
 * CreateRequest
 */
export type CreateRequest = {
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
 * CreateRequest without any key transformation, this is what
 * we expect to come in as network data
 */
export type External$CreateRequest = {
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
 * Takes network data, validates it, and transforms keys to match typescript object CreateRequest
 */
const SchemaIn$CreateRequest: z.ZodType<
  CreateRequest, // output type of this zod object
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
 * Takes typescript data, validates it, and maps keys to match the expected external object External$CreateRequest
 */
const SchemaOut$CreateRequest: z.ZodType<
  External$CreateRequest, // output type of this zod object
  z.ZodTypeDef,
  CreateRequest // the object to be transformed
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

export const Schemas$CreateRequest = {
  in: SchemaIn$CreateRequest,
  out: SchemaOut$CreateRequest,
};

/**
 * UpdateRequest
 */
export type UpdateRequest = {
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
  usernamePath: string;
};

/**
 * @internal
 * UpdateRequest without any key transformation, this is what
 * we expect to come in as network data
 */
export type External$UpdateRequest = {
  email?: string | undefined;
  firstName?: string | undefined;
  id?: number | undefined;
  lastName?: string | undefined;
  password?: string | undefined;
  phone?: string | undefined;
  userStatus?: number | undefined;
  username?: string | undefined;
  username_path: string;
};

/**
 * Takes network data, validates it, and transforms keys to match typescript object UpdateRequest
 */
const SchemaIn$UpdateRequest: z.ZodType<
  UpdateRequest, // output type of this zod object
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
    username_path: z.string(),
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
      username_path: "usernamePath",
    });
  });

/**
 * @internal
 * Takes typescript data, validates it, and maps keys to match the expected external object External$UpdateRequest
 */
const SchemaOut$UpdateRequest: z.ZodType<
  External$UpdateRequest, // output type of this zod object
  z.ZodTypeDef,
  UpdateRequest // the object to be transformed
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
    usernamePath: z.string(),
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
      usernamePath: "username_path",
    });
  });

export const Schemas$UpdateRequest = {
  in: SchemaIn$UpdateRequest,
  out: SchemaOut$UpdateRequest,
};
