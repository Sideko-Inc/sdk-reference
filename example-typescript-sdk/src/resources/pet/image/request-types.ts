import { UploadFile, zodTransform, zodUploadFile } from "my_petstore_ts/core";
import * as z from "zod";

/**
 * UploadRequest
 */
export type UploadRequest = {
  data: UploadFile;
  petId: number;
  additionalMetadata?: string | undefined;
};

/**
 * @internal
 * UploadRequest without any key transformation, this is what
 * we expect to come in as network data
 */
export type External$UploadRequest = {
  data: UploadFile;
  petId: number;
  additionalMetadata?: string | undefined;
};

/**
 * Takes network data, validates it, and transforms keys to match typescript object UploadRequest
 */
const SchemaIn$UploadRequest: z.ZodType<
  UploadRequest, // output type of this zod object
  z.ZodTypeDef,
  unknown
> = z
  .object({
    data: zodUploadFile,
    petId: z.number().int(),
    additionalMetadata: z.string().optional(),
  })
  .transform((obj) => {
    return zodTransform(obj, {
      data: "data",
      petId: "petId",
      additionalMetadata: "additionalMetadata",
    });
  });

/**
 * @internal
 * Takes typescript data, validates it, and maps keys to match the expected external object External$UploadRequest
 */
const SchemaOut$UploadRequest: z.ZodType<
  External$UploadRequest, // output type of this zod object
  z.ZodTypeDef,
  UploadRequest // the object to be transformed
> = z
  .object({
    data: zodUploadFile,
    petId: z.number().int(),
    additionalMetadata: z.string().optional(),
  })
  .transform((obj) => {
    return zodTransform(obj, {
      data: "data",
      petId: "petId",
      additionalMetadata: "additionalMetadata",
    });
  });

export const Schemas$UploadRequest = {
  in: SchemaIn$UploadRequest,
  out: SchemaOut$UploadRequest,
};
