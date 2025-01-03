import { zodTransform } from "my_petstore_ts/core";
import {
  External$OrderStatusEnum,
  OrderStatusEnum,
} from "my_petstore_ts/types/order-status-enum";
import * as z from "zod";

/**
 * DeleteRequest
 */
export type DeleteRequest = {
  orderId: number;
};

/**
 * @internal
 * DeleteRequest without any key transformation, this is what
 * we expect to come in as network data
 */
export type External$DeleteRequest = {
  orderId: number;
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
    orderId: z.number().int(),
  })
  .transform((obj) => {
    return zodTransform(obj, {
      orderId: "orderId",
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
    orderId: z.number().int(),
  })
  .transform((obj) => {
    return zodTransform(obj, {
      orderId: "orderId",
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
  orderId: number;
};

/**
 * @internal
 * GetRequest without any key transformation, this is what
 * we expect to come in as network data
 */
export type External$GetRequest = {
  orderId: number;
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
    orderId: z.number().int(),
  })
  .transform((obj) => {
    return zodTransform(obj, {
      orderId: "orderId",
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
    orderId: z.number().int(),
  })
  .transform((obj) => {
    return zodTransform(obj, {
      orderId: "orderId",
    });
  });

export const Schemas$GetRequest = {
  in: SchemaIn$GetRequest,
  out: SchemaOut$GetRequest,
};

/**
 * PlaceRequest
 */
export type PlaceRequest = {
  complete?: boolean | undefined;
  id?: number | undefined;
  petId?: number | undefined;
  quantity?: number | undefined;
  shipDate?: string | undefined;
  /**
   * Order Status
   */
  status?: OrderStatusEnum | undefined;
};

/**
 * @internal
 * PlaceRequest without any key transformation, this is what
 * we expect to come in as network data
 */
export type External$PlaceRequest = {
  complete?: boolean | undefined;
  id?: number | undefined;
  petId?: number | undefined;
  quantity?: number | undefined;
  shipDate?: string | undefined;
  status?: External$OrderStatusEnum | undefined;
};

/**
 * Takes network data, validates it, and transforms keys to match typescript object PlaceRequest
 */
const SchemaIn$PlaceRequest: z.ZodType<
  PlaceRequest, // output type of this zod object
  z.ZodTypeDef,
  unknown
> = z
  .object({
    complete: z.boolean().optional(),
    id: z.number().int().optional(),
    petId: z.number().int().optional(),
    quantity: z.number().int().optional(),
    shipDate: z.string().optional(),
    status: z.enum(["approved", "delivered", "placed"]).optional(),
  })
  .transform((obj) => {
    return zodTransform(obj, {
      complete: "complete",
      id: "id",
      petId: "petId",
      quantity: "quantity",
      shipDate: "shipDate",
      status: "status",
    });
  });

/**
 * @internal
 * Takes typescript data, validates it, and maps keys to match the expected external object External$PlaceRequest
 */
const SchemaOut$PlaceRequest: z.ZodType<
  External$PlaceRequest, // output type of this zod object
  z.ZodTypeDef,
  PlaceRequest // the object to be transformed
> = z
  .object({
    complete: z.boolean().optional(),
    id: z.number().int().optional(),
    petId: z.number().int().optional(),
    quantity: z.number().int().optional(),
    shipDate: z.string().optional(),
    status: z.enum(["approved", "delivered", "placed"]).optional(),
  })
  .transform((obj) => {
    return zodTransform(obj, {
      complete: "complete",
      id: "id",
      petId: "petId",
      quantity: "quantity",
      shipDate: "shipDate",
      status: "status",
    });
  });

export const Schemas$PlaceRequest = {
  in: SchemaIn$PlaceRequest,
  out: SchemaOut$PlaceRequest,
};
