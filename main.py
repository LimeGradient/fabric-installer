import os
import sys

# Usage: fabric-installer <dirname> <modid> <groupid>

if os.path.exists(sys.argv[1]) == False: # Checks for if fabric already installed to path
    os.system("git clone https://github.com/FabricMC/fabric-example-mod/")
    os.rename("fabric-example-mod", sys.argv[1])

with open(f"{sys.argv[1]}/gradle.properties", 'r') as gradProp: # Edit gradle.properties
    gradPropData = gradProp.readlines()

gradPropData[12] = f"maven_group={sys.argv[3]}\n"
gradPropData[13] = f"archives_base_name={sys.argv[2]}\n"

with open(f"{sys.argv[1]}/gradle.properties", 'w') as gradProp:
    gradProp.writelines(gradPropData)
print("gradle.properties successful")

group = sys.argv[3].split(".")

os.rename(f"{sys.argv[1]}/src/client/java/com", f"{sys.argv[1]}/src/client/java/{group[0]}")
os.rename(f"{sys.argv[1]}/src/client/java/{group[0]}/example", f"{sys.argv[1]}/src/client/java/{group[0]}/{group[1]}")
os.rename(f"{sys.argv[1]}/src/client/java/{group[0]}/{group[1]}/ExampleModClient.java", f"{sys.argv[1]}/src/client/java/{group[0]}/{group[1]}/{sys.argv[2]}Client.java")
os.rename(f"{sys.argv[1]}/src/client/java/{group[0]}/{group[1]}/mixin/client/ExampleClientMixin.java", f"{sys.argv[1]}/src/client/java/{group[0]}/{group[1]}/mixin/client/{sys.argv[2]}ClientMixin.java")
print("first rename successful")

with open(f"{sys.argv[1]}/src/client/java/{group[0]}/{group[1]}/{sys.argv[2]}Client.java", 'r') as mainJava:
    mainJavaData = mainJava.readlines()

mainJavaData[0] = f"package {group[0]}.{group[1]};\n"
mainJavaData[4] = f"public class {sys.argv[2]}Client implements ClientModInitializer {{\n"

with open(f"{sys.argv[1]}/src/client/java/{group[0]}/{group[1]}/{sys.argv[2]}Client.java", 'w') as mainJava:
    mainJava.writelines(mainJavaData)
print(f"{sys.argv[2]}Client.java edit successful")

with open(f"{sys.argv[1]}/src/client/java/{group[0]}/{group[1]}/mixin/client/{sys.argv[2]}ClientMixin.java", 'r') as mixinJava:
    mixinJavaData = mixinJava.readlines()

mixinJavaData[0] = f"package {group[0]}.{group[1]}.mixin.client;\n"
mixinJavaData[9] = f"public class {sys.argv[2]}ClientMixin {{\n"

with open(f"{sys.argv[1]}/src/client/java/{group[0]}/{group[1]}/mixin/client/{sys.argv[2]}ClientMixin.java", 'w') as mixinJava:
    mixinJava.writelines(mixinJavaData)
print(f"{sys.argv[2]}ClientMixin.java edit successful")

os.rename(f"{sys.argv[1]}/src/client/resources/modid.client.mixins.json", f"{sys.argv[1]}/src/client/resources/{sys.argv[2]}.client.mixins.json")
with open(f"{sys.argv[1]}/src/client/resources/{sys.argv[2]}.client.mixins.json", 'r') as clientMixin:
    clientMixinData = clientMixin.readlines()

clientMixinData[2] = f"\t\"package\": \"{group[0]}.{group[1]}.mixin.client\",\n"
clientMixinData[5] = f"\t\t\"{sys.argv[2]}ClientMixin\"\n"

with open(f"{sys.argv[1]}/src/client/resources/{sys.argv[2]}.client.mixins.json", 'w') as clientMixin:
    clientMixin.writelines(clientMixinData)
print(f"{sys.argv[2]}.client.mixins.json edit successful")

os.rename(f"{sys.argv[1]}/src/main/java/com", f"{sys.argv[1]}/src/main/java/{group[0]}")
os.rename(f"{sys.argv[1]}/src/main/java/{group[0]}/example", f"{sys.argv[1]}/src/main/java/{group[0]}/{group[1]}")
os.rename(f"{sys.argv[1]}/src/main/java/{group[0]}/{group[1]}/ExampleMod.java", f"{sys.argv[1]}/src/main/java/{group[0]}/{group[1]}/{sys.argv[2]}.java")
os.rename(f"{sys.argv[1]}/src/main/java/{group[0]}/{group[1]}/mixin/ExampleMixin.java", f"{sys.argv[1]}/src/main/java/{group[0]}/{group[1]}/mixin/{sys.argv[2]}Mixin.java")
print("second rename successful")

with open(f"{sys.argv[1]}/src/main/java/{group[0]}/{group[1]}/{sys.argv[2]}.java", 'r') as mainJava:
    mainJavaData = mainJava.readlines()

mainJavaData[0] = f"package {group[0]}.{group[1]};\n"
mainJavaData[7] = f"public class {sys.argv[2]} implements ModInitializer {{\n"

with open(f"{sys.argv[1]}/src/main/java/{group[0]}/{group[1]}/{sys.argv[2]}.java", 'w') as mainJava:
    mainJava.writelines(mainJavaData)
print(f"{sys.argv[2]}.java edit successful")

with open(f"{sys.argv[1]}/src/main/java/{group[0]}/{group[1]}/mixin/{sys.argv[2]}Mixin.java", 'r') as mixinJava:
    mixinJavaData = mixinJava.readlines()

mixinJavaData[0] = f"package {group[0]}.{group[1]}.mixin;\n"
mixinJavaData[9] = f"public class {sys.argv[2]}Mixin {{\n"

with open(f"{sys.argv[1]}/src/main/java/{group[0]}/{group[1]}/mixin/{sys.argv[2]}Mixin.java", 'w') as mixinJava:
    mixinJava.writelines(mixinJavaData)
print(f"{sys.argv[2]}Mixin.java edit successful")

os.rename(f"{sys.argv[1]}/src/main/resources/assets/modid", f"{sys.argv[1]}/src/main/resources/assets/{sys.argv[2]}")
os.rename(f"{sys.argv[1]}/src/main/resources/modid.mixins.json", f"{sys.argv[1]}/src/main/resources/{sys.argv[2]}.mixins.json")
with open(f"{sys.argv[1]}/src/main/resources/fabric.mod.json", 'r') as fabricJson:
    fabricJsonData = fabricJson.readlines()

fabricJsonData[2] = f"\t\"id\": \"{sys.argv[2]}\",\n"
fabricJsonData[14] = f"\t\"icon\": \"assets/{sys.argv[2]}/icon.png\",\n"
fabricJsonData[18] = f"\t\t\t{group[0]}.{group[1]}.{sys.argv[2]}\n"
fabricJsonData[21] = f"\t\t\t{group[0]}.{group[1]}.{sys.argv[2]}Client\n"
fabricJsonData[25] = f"\t\t\"{sys.argv[2]}.mixins.json\",\n"
fabricJsonData[27] = f"\t\"config\": \"{sys.argv[2]}.client.mixins.json\",\n"

with open(f"{sys.argv[1]}/src/main/resources/fabric.mod.json", 'w') as fabricJson:
    fabricJson.writelines(fabricJsonData)
print("fabric.mod.json edit successful")

with open(f"{sys.argv[1]}/src/main/resources/{sys.argv[2]}.mixins.json", 'r') as mixinsJson:
    mixinsJsonData = mixinsJson.readlines()

mixinsJsonData[2] = f"\t\"package\": \"{group[0]}.{group[1]}.mixin\",\n"
mixinsJsonData[5] = f"\t\t\"{sys.argv[2]}Mixin\"\n"

with open(f"{sys.argv[1]}/src/main/resources/{sys.argv[2]}.mixins.json", 'w') as mixinsJson:
    mixinsJson.writelines(mixinsJsonData)
print(f"{sys.argv[2]}.mixins.json edit successful")
print("All Edits Successful! Project is now ready. Happy Modding!")