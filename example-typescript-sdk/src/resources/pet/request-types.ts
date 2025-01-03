import { zodTransform } from "my_petstore_ts/core";
import {
  Category,
  External$Category,
  Schemas$Category,
} from "my_petstore_ts/types/category";
import {
  External$PetStatusEnum,
  PetStatusEnum,
} from "my_petstore_ts/types/pet-status-enum";
import { External$Tag, Schemas$Tag, Tag } from "my_petstore_ts/types/tag";
import * as z from "zod";

/**
 * DeleteRequest
 */
export type DeleteRequest = {
  petId: number;
};

/**
 * @internal
 * DeleteRequest without any key transformation, this is what
 * we expect to come in as network data
 */
export type External$DeleteRequest = {
  petId: number;
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
    petId: z.number().int(),
  })
  .transform((obj) => {
    return zodTransform(obj, {
      petId: "petId",
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
    petId: z.number().int(),
  })
  .transform((obj) => {
    return zodTransform(obj, {
      petId: "petId",
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
  petId: number;
};

/**
 * @internal
 * GetRequest without any key transformation, this is what
 * we expect to come in as network data
 */
export type External$GetRequest = {
  petId: number;
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
    petId: z.number().int(),
  })
  .transform((obj) => {
    return zodTransform(obj, {
      petId: "petId",
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
    petId: z.number().int(),
  })
  .transform((obj) => {
    return zodTransform(obj, {
      petId: "petId",
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
  category?: Category | undefined;
  id?: number | undefined;
  name: string;
  photoUrls: string[];
  /**
   * pet status in the store
   */
  status?: PetStatusEnum | undefined;
  tags?: Tag[] | undefined;
};

/**
 * @internal
 * CreateRequest without any key transformation, this is what
 * we expect to come in as network data
 */
export type External$CreateRequest = {
  category?: External$Category | undefined;
  id?: number | undefined;
  name: string;
  photoUrls: string[];
  status?: External$PetStatusEnum | undefined;
  tags?: External$Tag[] | undefined;
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
    category: Schemas$Category.in.optional(),
    id: z.number().int().optional(),
    name: z.string(),
    photoUrls: z.array(z.string()),
    status: z.enum(["available", "pending", "sold"]).optional(),
    tags: z.array(Schemas$Tag.in).optional(),
  })
  .transform((obj) => {
    return zodTransform(obj, {
      category: "category",
      id: "id",
      name: "name",
      photoUrls: "photoUrls",
      status: "status",
      tags: "tags",
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
    category: Schemas$Category.out.optional(),
    id: z.number().int().optional(),
    name: z.string(),
    photoUrls: z.array(z.string()),
    status: z.enum(["available", "pending", "sold"]).optional(),
    tags: z.array(Schemas$Tag.out).optional(),
  })
  .transform((obj) => {
    return zodTransform(obj, {
      category: "category",
      id: "id",
      name: "name",
      photoUrls: "photoUrls",
      status: "status",
      tags: "tags",
    });
  });

export const Schemas$CreateRequest = {
  in: SchemaIn$CreateRequest,
  out: SchemaOut$CreateRequest,
};

/**
 * UpdateFormRequest
 */
export type UpdateFormRequest = {
  petId: number;
  name?: string | undefined;
  status?: string | undefined;
};

/**
 * @internal
 * UpdateFormRequest without any key transformation, this is what
 * we expect to come in as network data
 */
export type External$UpdateFormRequest = {
  petId: number;
  name?: string | undefined;
  status?: string | undefined;
};

/**
 * Takes network data, validates it, and transforms keys to match typescript object UpdateFormRequest
 */
const SchemaIn$UpdateFormRequest: z.ZodType<
  UpdateFormRequest, // output type of this zod object
  z.ZodTypeDef,
  unknown
> = z
  .object({
    petId: z.number().int(),
    name: z.string().optional(),
    status: z.string().optional(),
  })
  .transform((obj) => {
    return zodTransform(obj, {
      petId: "petId",
      name: "name",
      status: "status",
    });
  });

/**
 * @internal
 * Takes typescript data, validates it, and maps keys to match the expected external object External$UpdateFormRequest
 */
const SchemaOut$UpdateFormRequest: z.ZodType<
  External$UpdateFormRequest, // output type of this zod object
  z.ZodTypeDef,
  UpdateFormRequest // the object to be transformed
> = z
  .object({
    petId: z.number().int(),
    name: z.string().optional(),
    status: z.string().optional(),
  })
  .transform((obj) => {
    return zodTransform(obj, {
      petId: "petId",
      name: "name",
      status: "status",
    });
  });

export const Schemas$UpdateFormRequest = {
  in: SchemaIn$UpdateFormRequest,
  out: SchemaOut$UpdateFormRequest,
};

/**
 * UpdateRequest
 */
export type UpdateRequest = {
  category?: Category | undefined;
  id?: number | undefined;
  name: string;
  photoUrls: string[];
  /**
   * pet status in the store
   */
  status?: PetStatusEnum | undefined;
  tags?: Tag[] | undefined;
};

/**
 * @internal
 * UpdateRequest without any key transformation, this is what
 * we expect to come in as network data
 */
export type External$UpdateRequest = {
  category?: External$Category | undefined;
  id?: number | undefined;
  name: string;
  photoUrls: string[];
  status?: External$PetStatusEnum | undefined;
  tags?: External$Tag[] | undefined;
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
    category: Schemas$Category.in.optional(),
    id: z.number().int().optional(),
    name: z.string(),
    photoUrls: z.array(z.string()),
    status: z.enum(["available", "pending", "sold"]).optional(),
    tags: z.array(Schemas$Tag.in).optional(),
  })
  .transform((obj) => {
    return zodTransform(obj, {
      category: "category",
      id: "id",
      name: "name",
      photoUrls: "photoUrls",
      status: "status",
      tags: "tags",
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
    category: Schemas$Category.out.optional(),
    id: z.number().int().optional(),
    name: z.string(),
    photoUrls: z.array(z.string()),
    status: z.enum(["available", "pending", "sold"]).optional(),
    tags: z.array(Schemas$Tag.out).optional(),
  })
  .transform((obj) => {
    return zodTransform(obj, {
      category: "category",
      id: "id",
      name: "name",
      photoUrls: "photoUrls",
      status: "status",
      tags: "tags",
    });
  });

export const Schemas$UpdateRequest = {
  in: SchemaIn$UpdateRequest,
  out: SchemaOut$UpdateRequest,
};
